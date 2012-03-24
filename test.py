import pyglet

window = pyglet.window.Window()


@window.event
def on_mouse_motion(mouseX, mouseY, dx, dy):
	x = (mouseX - window.width / 2) / 4.0
	y = (mouseY - window.height / 2) / 4.0

	print("x: %s, y: %s" % (x, y))
	player.position = (x, y, 0)

@window.event
def on_draw():
	window.clear()
	sprite.set_position(0, 0)
	sprite.draw()


event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_enter():
	global player, image, sprite
	player = pyglet.media.Player()
	player.eos_action = player.EOS_LOOP
	player.queue(pyglet.media.load('loop.wav', streaming=False))
	player.play()

	image = pyglet.image.load('crosshairs.png')
	sprite = pyglet.sprite.Sprite(image)

event_loop.run()
