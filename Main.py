import arcade
from arcade.color import GREEN, RED, SKY_BLUE, YELLOW

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Kiwi(arcade.Sprite):
    def __init__(self, image):
        scaling_factor = 0.18
        super().__init__(image, scaling_factor)

        self.center_x = 0
        self.center_y = 0

        self.speed_x = 5
        self.speed_y = 5

        self.left = False
        self.right = False
    
    def update(self):

        print(self.center_x, self.center_y)
        if self.left:
            self.center_x -= self.speed_x
        if self.right:
            self.center_x += self.speed_x
    

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "User Controll")
        self.set_mouse_visible(False)
        self.kiwi = Kiwi('Images/kiwi_default.png')

    def on_draw(self):
        arcade.set_background_color(SKY_BLUE)
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0,599, 200, 0, GREEN)
        self.kiwi.draw()
    
    def on_update(self, delta_time):
        self.kiwi.update()
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left = True
        elif key == arcade.key.RIGHT:
            self.right = True
        
        
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left = False
        if key == arcade.key.RIGHT:
            self.right = False


def main():
    window = MyGame()
    arcade.run()

main()

