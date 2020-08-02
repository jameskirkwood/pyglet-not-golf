import pyglet, res

class Mass(pyglet.sprite.Sprite):
	def __init__(self, x=256, y=380, mass=1, scale=0.5, batch=None):
		super(type(self),self).__init__(img=res.mass, x=x, y=y, batch=batch)
		self.scale=scale
		self.mass=mass
		self.inx=x
		self.iny=y
		self.vx=0
		self.vy=0

	def tick(self, dt):
		self.x+=self.vx
		self.y+=self.vy
		if self.x<0:
			self.x+=512
		elif self.x>512:
			self.x-=512
		if self.y<0:
			self.y+=750
		elif self.y>750:
			self.y-=750

	def interact(self, obj):
		pass

	def reset(self):
		self.x,self.y=self.inx,self.iny
		self.vx=0
		self.vy=0