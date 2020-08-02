import pyglet, level

def restart(win, batch=None):
	lvl_disp=pyglet.text.Label(text='Level 1',x=win.width/2-27,y=win.height-15,batch=batch)
	lvl_state=['idle']
	alevel=level.Level(win, batch=batch)
	alevel.load([[256,60],
		['wall',0,375,90,0.66],
		['wall',512,375,90,0.66],
		['wall',500,400,-25,0.5],
		['wall',256,0,0,0.66],
		['wall',256,750,0,0.66],
		['wall',200,360,65,0.2],
		['wall',192,352,65,0.04,(0,255,0)],
		
		['mass',340,150,2000,0.1],
		['mass',260,560,5000,0.2]])

	win.register_event_type('game_event')

	@win.event
	def on_mouse_press(x, y, button, modifiers):
		if lvl_state[0]=='idle':
			pyglet.clock.schedule_interval(alevel.tick,1.0/60)
			lvl_state[0]='simulating'
		alevel.reset(x,y)

	@win.event
	def game_event(typ):
		if typ=='goal':
			pyglet.clock.unschedule()

	@win.event
	def on_key_press(symbol, modifiers):
		if lvl_state[0]=='simulating':
			if symbol==pyglet.window.key.SPACE:
				alevel.control_object.boost()