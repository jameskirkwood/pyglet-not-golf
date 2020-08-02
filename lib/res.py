import pyglet

pyglet.resource.path=["res"]
print(pyglet.resource.reindex())

mass=pyglet.resource.image("planet.png")
ball=pyglet.resource.image("ball.png")
moon=pyglet.resource.image("moon.png")
wall=pyglet.resource.image("wall.png")

def imgRotCentre(image):
	image.anchor_x=image.width/2
	image.anchor_y=image.height/2

for image in [mass,ball,moon,wall]:
	imgRotCentre(image)