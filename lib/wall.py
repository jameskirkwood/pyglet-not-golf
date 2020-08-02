import pyglet, res

class Wall(pyglet.sprite.Sprite):
	def __init__(self, x=256, y=380, rotation=0, scale=0.1, batch=None):
		super(type(self),self).__init__(img=res.wall, x=x, y=y, batch=batch)
		self.scale=scale
		self.rotation=rotation

	def tick(self, dt):
		pass

	def interact(self, obj):
		pass

	def reset(self):
		pass