from pyglet.window import Window
from pyglet import app

from pyglet.window import key
from pyglet.shapes import Circle


class Win(Window):

    def __init__(self, *args, **kwargs):
        super(Win, self).__init__(*args, **kwargs)
        self.setup()

    def setup(self):
        self.set_caption("Custom Renderer")
        self.character_sprite = Circle(100, 100, 5)
        self.speed = 10
        self.trail_length = 15

        self.character_sprite.x = self.width // 2
        self.character_sprite.y = self.height // 2
        self.character_movement = {"up": False, "down": False, "left": False, "right": False}
        self.trails = []


    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.close()

    def on_draw(self):
        self.update(1/60)
        self.clear()
        for trail in self.trails:
            Circle(trail[0], trail[1], 1).draw()
        self.character_sprite.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            self.character_movement["up"] = True
        elif symbol == key.A:
            self.character_movement["left"] = True
        elif symbol == key.S:
            self.character_movement["down"] = True
        elif symbol == key.D:
            self.character_movement["right"] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.W:
            self.character_movement["up"] = False
        elif symbol == key.A:
            self.character_movement["left"] = False
        elif symbol == key.S:
            self.character_movement["down"] = False
        elif symbol == key.D:
            self.character_movement["right"] = False

    def update(self, dt):
        self.character_sprite.x += self.speed if self.character_movement["right"] else 0
        self.character_sprite.x -= self.speed if self.character_movement["left"] else 0
        self.character_sprite.y += self.speed if self.character_movement["up"] else 0
        self.character_sprite.y -= self.speed if self.character_movement["down"] else 0
        self.trails.append((self.character_sprite.x, self.character_sprite.y))
        self.trails = self.trails[-self.trail_length:]  # keep only the last 100 points


if __name__ == '__main__':
    window = Win(800, 600, resizable=True)
    app.run()
