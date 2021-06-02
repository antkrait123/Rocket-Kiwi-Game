import arcade
from arcade.color import GREEN, RED, SKY_BLUE, YELLOW
from pyglet.window.key import SPACE

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
Kiwi_speed = 5
kiwi_scaling = 0.18

'''class Kiwi:
    def __init__(self, position_x, change_x, position_y, change_y ):
        self.position_x = position_x
        self.change_x = change_x
        self.position_y = position_y
        self.change_y = change_y
        
    

    def update(self):
        self.position_y = self.position_y + self.change_y 
        self.position_x = self.position_x + self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
        if self.position_y < self.radius:
            self.position_y = self.radius
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius '''

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "User Controll")
        self.set_mouse_visible(False)
        self.kiwi = arcade.Sprite("kiwi_default.png", kiwi_scaling)

    def on_draw(self):
        arcade.set_background_color(SKY_BLUE)
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0,599, 200, 0, GREEN)
        self.kiwi.draw()
    
    def update(self, delta_time):
        self.kiwi.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.kiwi.change_x = -Kiwi_speed
        elif key == arcade.key.RIGHT:
            self.kiwi.change_x = Kiwi_speed
        elif key == arcade.key.UP:
            self.kiwi.change_y = Kiwi_speed
        elif key == arcade.key.DOWN:
            self.kiwi.change_y = -Kiwi_speed
        
        
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.kiwi.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.kiwi.change_y = 0
        

def main():
    window = MyGame()
    arcade.run()

main()
