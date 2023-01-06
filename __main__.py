from pyglet.window import Window
from pyglet import app

from pyglet.window import key
from pyglet.gui import PushButton


class Win(Window):
    def __init__(self, *args, **kwargs):
        super(Win, self).__init__(*args, **kwargs)
        self.setup()

    def setup(self):
        self.set_caption("Custom Renderer")

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.close()

    def on_draw(self):
        self.clear()


if __name__ == '__main__':
    window = Win(800, 600, resizable=True)
    app.run()
