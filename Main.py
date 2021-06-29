import arcade
from arcade.color import BLACK, GREEN, RED, SKY_BLUE, YELLOW


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ROCKET KIWI"
MOVMENT_SPEED = 5

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
        window.draw()


class GamePlay(arcade.View):

    def __init__(self):
        super().__init__()
        self.player_list = None
        self.wall_list = None  
        self.player_sprite = None

        self.window.set_mouse_visible(False)
        #self.kiwi = Kiwi('Images/kiwi_default.png')
        


        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list)





    
    def setup(self):
        arcade.set_background_color(SKY_BLUE)

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        #create kiwi
        self.player_sprite = arcade.Sprite("Images.kiwi_default.png", 0.18)
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = 250 #SCREEN_HEIGHT/2#
        self.player_list.append(self.player_sprite)

       
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

    # --- Place boxes inside a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


        


    def on_draw(self):
        
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()
        arcade.draw_lrtb_rectangle_filled(0,799, 200, 0, GREEN)
        arcade.draw_lrtb_rectangle_filled(550,625,250,200, BLACK)
        #self.kiwi.draw()

    
    def on_update(self, delta_time):
        #self.kiwi.update()
        self.physics_engine.update()
        

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MenuScreen()
    window.show_view(start_view)
    arcade.run()

main()