import arcade
from arcade.color import GREEN, RED, SKY_BLUE, YELLOW


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
KIWI_SPEED = 5


class Kiwi(arcade.Sprite):
    def __init__(self, image):
        scaling_factor = 0.18
        super().__init__(image, scaling_factor)
        


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Rocket Kiwi")
        self.set_mouse_visible(False)
        self.kiwi = Kiwi('Images/kiwi_default.png')
        self.kiwi.center_x = SCREEN_WIDTH/2
        self.kiwi.center_y = SCREEN_HEIGHT/2

    def on_draw(self):
        arcade.set_background_color(SKY_BLUE)
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0,799, 200, 0, GREEN)
        self.kiwi.draw()
    
    def on_update(self, delta_time):
        self.kiwi.update()
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.kiwi.change_y = KIWI_SPEED
        elif key == arcade.key.DOWN:
            self.kiwi.change_y = -KIWI_SPEED
        elif key == arcade.key.LEFT:
            self.kiwi.change_x = -KIWI_SPEED
        elif key == arcade.key.RIGHT:
            self.kiwi.change_x = KIWI_SPEED
        
        
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or arcade.key.DOWN:
            self.kiwi.change_y = 0
        if key == arcade.key.RIGHT or arcade.key.LEFT:
            self.kiwi.change_x = 0


def main():
    window = MyGame()
    arcade.run()

main()