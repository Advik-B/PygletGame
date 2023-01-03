from pyglet.window import Window
from pyglet import app

window = Window()

@window.event
def on_draw():
    window.clear()

app.run()
