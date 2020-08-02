import pyglet
from . import ball, wall, mass

class Level():
	def __init__(self, win, batch=None):
		self.batch=batch
		self.win=win

	def load(self, data):
		self.control_object=ball.Ball(x=data[0][0], y=data[0][1], batch=self.batch)
		self.world_objects=[self.control_object]
		for each in data[1:]:
			if each[0]=='wall':
				self.world_objects.append(wall.Wall(x=each[1],y=each[2],rotation=each[3],scale=each[4],batch=self.batch))
				if len(each)>5:
					self.world_objects[-1].color=each[5]
			elif each[0]=='mass':
				self.world_objects.append(mass.Mass(x=each[1],y=each[2],mass=each[3],scale=each[4],batch=self.batch))

	def tick(self, dt):
		for each in self.world_objects:
			each.tick(dt)
			for erch in self.world_objects:
				if each!=erch:
					each.interact(erch)

	def reset(self, x, y):
		for each in self.world_objects:
			each.reset()
		vx=(x-self.control_object.inx)*0.04
		vy=(y-self.control_object.iny)*0.04
		magv=(vx**2+vy**2)**0.5
		if magv>10:
			vx*=10.0/magv
			vy*=10.0/magv
		self.control_object.vx=vx
		self.control_object.vy=vy