import arcade
from arcade.color import GREEN, RED, SKY_BLUE

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Ball:
    def __init__(self, position_x, position_y, radius, colour):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.colour = colour
    
    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.colour)


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "User Controll")
        self.ball = Ball(300, 500, 35, RED)

    def on_draw(self):
        arcade.set_background_color(SKY_BLUE)
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0,599, 200, 0, GREEN)
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.position_x = x
        self.ball.position_y = y


def main():
    window = MyGame()
    arcade.run()

main()