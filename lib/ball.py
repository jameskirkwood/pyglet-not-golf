import pyglet, res, util, math

class Ball(pyglet.sprite.Sprite):
	def __init__(self, x=256, y=10, batch=None):
		super(type(self),self).__init__(img=res.moon, x=x, y=y, batch=batch)
		self.scale=0.4
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

	def reflect(self, angle, x, y, d):
		relv=util.rot((self.vx,self.vy),-angle)
		relp=util.rot((self.x-x,self.y-y),-angle)
		new_relx=math.copysign(d,relp[0])
		relp=(new_relx,relp[1]+(new_relx-relp[0])*(relv[1]/relv[0]))
		self.x,self.y=util.addv(util.rot(relp,angle),(x,y))
		self.vx,self.vy=util.rot((-relv[0],relv[1]),angle)

	def interact(self, obj):
		import wall, mass
		dx=self.x-obj.x
		dy=self.y-obj.y
		d=(dx**2+dy**2)**0.5

		if type(obj)==wall.Wall and d<576*obj.scale+6.6:
			relp=util.rot((self.x-obj.x,self.y-obj.y),-obj.rotation)
			if math.fabs(relp[0])<576*obj.scale:
				if math.fabs(relp[1])<45.5*obj.scale+6.6:
					self.reflect(obj.rotation-90,obj.x,obj.y,45.5*obj.scale+6.6)
					self.vx*=0.9
					self.vy*=0.9
			elif math.fabs(relp[1])<45.5*obj.scale:
				if math.fabs(relp[0])<576*obj.scale+6.6:
					self.reflect(obj.rotation,obj.x,obj.y,576*obj.scale+6.6)
					self.vx*=0.9
					self.vy*=0.9

		elif type(obj)==mass.Mass:
			if d<129.5*obj.scale+6.6:
				self.reflect(util.ang((dx,dy)), obj.x, obj.y, 129.5*obj.scale+6.6)
				self.vx*=0.7
				self.vy*=0.7
				dx=self.x-obj.x
				dy=self.y-obj.y
				sf=(129.5*obj.scale+6.6)/math.hypot(dx,dy)
				self.x=obj.x+dx*sf
				self.y=obj.y+dy*sf
			elif d>129.5*obj.scale+7:
				F=float(obj.mass)/d**2
				self.vx-=(dx/d)*F
				self.vy-=(dy/d)*F
			else:
				self.vx*=0.5
				self.vy*=0.5

	def reset(self):
		self.x,self.y=self.inx,self.iny
		self.vx=0
		self.vy=0

	def boost(self):
		self.vx*=1.3
		self.vy*=1.3