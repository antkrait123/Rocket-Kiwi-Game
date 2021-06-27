import arcade
from arcade.color import BLACK, GREEN, RED, SKY_BLUE, YELLOW


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ROCKET KIWI"
KIWI_SPEED = 5

#JUMP_SPEED = 5#

BOX_SCALING = 5.5

#class Kiwi(arcade.Sprite):
#    def __init__(self, image):
#        scaling_factor = 0.18
#        super().__init__(image, scaling_factor)


class MenuScreen(arcade.View):

    def on_show(self):
        arcade.set_background_color(RED)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("MENU" , SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, font_size = 50, anchor_x="center")
        arcade.draw_text("Click here to start...", SCREEN_WIDTH/2 + 10, SCREEN_HEIGHT/2 - 50, arcade.color.BLACK, font_size = 20, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GamePlay()
        self.window.show_view(game_view)
        window.setup()


class GamePlay(arcade.View):

    def __init__(self):
        super().__init__()
        self.player_list = None
        self.wall_list = None  
        self.player_sprite = None

        self.window.set_mouse_visible(False)
        #self.kiwi = Kiwi('Images/kiwi_default.png')
        


        #self.physics_engine = arcade.PhysicsEnginePlatformer(self.kiwi, self.wall_list)





    
    def setup(self):
        arcade.set_background_color(SKY_BLUE)

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        #create kiwi
        self.player_sprite = arcade.Sprite("Images.kiwi_default.png", 0.18)
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = 250 #SCREEN_HEIGHT/2#
        self.player_list.append(self.kiwi_sprite)

       
        # Manually create and position a box at 300, 200
        wall = arcade.Sprite("Images/box.png", BOX_SCALING)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        # Manually create and position a box at 364, 200
        wall = arcade.Sprite("Images/box.png", BOX_SCALING)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

        


    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0,799, 200, 0, GREEN)
        arcade.draw_lrtb_rectangle_filled(550,625,250,200, BLACK)
        self.kiwi.draw()

        self.wall_list.draw()
    
    def on_update(self, delta_time):
        self.kiwi.update()
        self.physics_engine.update()
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump(y_distance=5):
            #self.kiwi.change_y = KIWI_SPEED#
            self.kiwi.change_y = JUMP_SPEED
        #if key == arcade.key.DOWN:
            #self.kiwi.change_y = -KIWI_SPEED
        if key == arcade.key.LEFT:
            self.kiwi.change_x = -KIWI_SPEED
        if key == arcade.key.RIGHT:
            self.kiwi.change_x = KIWI_SPEED
        
        
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or arcade.key.DOWN:
            self.kiwi.change_y = 0
        if key == arcade.key.RIGHT or arcade.key.LEFT:
            self.kiwi.change_x = 0


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MenuScreen()
    window.show_view(start_view)
    arcade.run()

main()