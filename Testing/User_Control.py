import arcade
from arcade.color import GREEN, RED, SKY_BLUE, YELLOW

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BALL_SPEED = 7

class Ball:
    def __init__(self, position_x, change_x, position_y, change_y, radius, colour):
        self.position_x = position_x
        self.change_x = change_x
        self.position_y = position_y
        self.change_y = change_y
        self.radius = radius
        self.colour = colour
    
    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.colour)

    def update(self):
        self.position_y = self.position_y + self.change_y 
        self.position_x = self.position_x + self.change_x

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "User Controll")
        self.set_mouse_visible(False)
        self.ball = Ball(300, 0, 500, 0, 30, RED)

    def on_draw(self):
        arcade.set_background_color(SKY_BLUE)
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0,599, 200, 0, GREEN)
        self.ball.draw()
    
    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.change_x = -BALL_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = BALL_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = BALL_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -BALL_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


    
def main():
    window = MyGame()
    arcade.run()

main()
