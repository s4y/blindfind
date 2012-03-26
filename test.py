import pyglet

window = pyglet.window.Window(width=670, height=669)


@window.event
def on_mouse_motion(mouseX, mouseY, dx, dy):
	x = (mouseX - window.width / 2) / 20.0
	y = (mouseY - window.height / 2) / 20.0

	print("x: %s, y: %s" % (x, y))

	player.position = (x, y, 0)

@window.event
def on_draw():
	window.clear()
	sprite.set_position(0, 0)
	image.blit(0, 0)


event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_enter():
	global player, image, sprite
	player = pyglet.media.Player()
	player.eos_action = player.EOS_LOOP
	player.queue(pyglet.media.load('loop.wav', streaming=False))
	player.play()

	image = pyglet.image.load('crosshairs.png')
	sprite = pyglet.sprite.Sprite(image, x=200, y=200)
	sprite.opacity = 1

pyglet.gl.glClearColor(1, 1, 1, 1)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
event_loop.run()
