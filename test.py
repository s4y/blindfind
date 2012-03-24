import pyglet

player = pyglet.media.Player()
player.queue(pyglet.media.load('loop.wav', streaming=False))
player.eos_action = player.EOS_LOOP
player.play()

window = pyglet.window.Window()

image = pyglet.image.load('crosshairs.png')
sprite = pyglet.sprite.Sprite(image)

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

pyglet.app.run()
