from pyglet.window import Window
from pyglet import app

from pyglet.window import key
from pyglet.shapes import Circle, Line


class Win(Window):

    def __init__(self, *args, **kwargs):
        super(Win, self).__init__(*args, **kwargs)
        self.setup()

    def setup(self):
        self.set_caption("PyGlet Graphics Project")
        self.character_sprite = Circle(100, 100, 5)
        # Yellow
        self.character_sprite.color = (255, 255, 0)
        self.speed = 10
        self.trail_length = 15
        self.mouse_mode = False

        self.character_sprite.x = self.width // 2
        self.character_sprite.y = self.height // 2
        self.character_movement = {"up": False, "down": False, "left": False, "right": False}
        self.trails = []
        self.grid_size = 10
        self.grid_color = (255, 255, 255)
        self.grid_width = 1
        self.grid_height = 1
        self.grid_spacing = 100


        self.notis = None
        self.grid_mode = False
        self.trails_enabled = True
        self.setup_grid()

    def setup_grid(self):
        self.grid = [
            Line(x, 0, x, self.height, self.grid_width, self.grid_color)
            for x in range(0, self.width, self.grid_spacing)
        ]
        self.grid.extend(
            Line(0, y, self.width, y, self.grid_width, self.grid_color)
            for y in range(0, self.height, self.grid_spacing)
        )

    def draw_trails(self):
        for trail in self.trails:
            Circle(trail[0], trail[1], 1).draw()

    def draw_grid(self):
        for line in self.grid:
            line.draw()

    def on_draw(self):
        self.update()
        self.clear()
        self.character_sprite.draw()
        if self.trails_enabled:
            self.draw_trails()
        if self.grid_mode:
            self.draw_grid()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            self.character_movement["up"] = True
        elif symbol == key.A:
            self.character_movement["left"] = True
        elif symbol == key.S:
            self.character_movement["down"] = True
        elif symbol == key.D:
            self.character_movement["right"] = True

        elif symbol == key.ESCAPE:
            self.close()

    def on_key_release(self, symbol, modifiers):
        if symbol == key.W:
            self.character_movement["up"] = False
        elif symbol == key.A:
            self.character_movement["left"] = False
        elif symbol == key.S:
            self.character_movement["down"] = False
        elif symbol == key.D:
            self.character_movement["right"] = False
        elif symbol == key.M:
            self.mouse_mode = not self.mouse_mode
            # Mouse should be locked to the window and invisible
            self.set_exclusive_mouse(self.mouse_mode)
            self.set_mouse_visible(not self.mouse_mode)

        elif symbol == key.R:
            self.setup()

        elif symbol == key.G:
            self.grid_mode = not self.grid_mode

        elif symbol == key.EQUAL:
            print("Increasing grid spacing")
            self.grid_spacing += 1
            self.setup_grid()

        elif symbol == key.MINUS:
            print("Decreasing grid spacing")
            self.grid_spacing -= 1
            self.grid_spacing = max(1, self.grid_spacing)
            self.setup_grid()

        elif symbol == key.T:
            # Disable trails
            self.trails_enabled = not self.trails_enabled

        elif symbol == key.SPACE:
            # Increase trail length
            self.trail_length += 1

        elif symbol == key.BACKSPACE:
            # Decrease trail length
            self.trail_length -= 1
            self.trail_length = max(1, self.trail_length)

    def reduce_trails(self):
        self.trails.append((self.character_sprite.x, self.character_sprite.y))
        self.trails = self.trails[-self.trail_length:]  # keep only the last 100 points

    def update(self, dt: float = 1 / 60):
        if not self.mouse_mode:
            self.character_sprite.x += self.speed if self.character_movement["right"] else 0
            self.character_sprite.x -= self.speed if self.character_movement["left"] else 0
            self.character_sprite.y += self.speed if self.character_movement["up"] else 0
            self.character_sprite.y -= self.speed if self.character_movement["down"] else 0
        self.reduce_trails()

    def on_mouse_motion(self, x, y, dx, dy):
        if self.mouse_mode:
            self.character_sprite.x = dx + self.character_sprite.x
            self.character_sprite.y = dy + self.character_sprite.y

    def on_resize(self, width, height):
        super(Win, self).on_resize(width, height)
        self.setup_grid()


if __name__ == '__main__':
    window = Win(800, 600, resizable=True)
    app.run()
