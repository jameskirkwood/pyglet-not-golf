import pyglet
from lib import res, game

# // init window // #

win=pyglet.window.Window(512,750,caption='Quantum Minigolf')
gbat_hud=pyglet.graphics.Batch()
gbat_world=pyglet.graphics.Batch()

@win.event
def on_draw():
	win.clear()
	gbat_world.draw()
	gbat_hud.draw()

# // init  world // #

game.restart(win, batch=gbat_world)

# // start  game // #

print '\nQUANTUM MINIGOLF STARTED\n'
if __name__=='__main__':
	pyglet.app.run()