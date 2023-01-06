import contextlib
from pyglet.window import Window
from pyglet import app

import pyglet


class GameWindow(Window):
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)
        self.message: pyglet.text.Label = None
        self.setup()

    def setup(self):
        self.message = pyglet.text.Label(
            "Go ahead, Hover over me!",
            font_name="JetBrains Mono",
            font_size=36,
            x=self.width // 2,
            y=self.height // 2,
            anchor_x="center",
            anchor_y="center",
        )
        self.set_caption("My Game")

    def on_draw(self):
        self.clear()
        self.message.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        with contextlib.suppress(ValueError):
            self.set_size(x, y)
        self.set_location(x, y)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self.close()


if __name__ == '__main__':
    window = GameWindow(800, 600, resizable=True)
    app.run()
