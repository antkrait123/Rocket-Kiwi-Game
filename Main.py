import arcade
from arcade.color import BLACK, GREEN, RED, SKY_BLUE, YELLOW


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ROCKET KIWI"
MOVEMENT_SPEED = 10

VIEWPORT_MARGIN = 40

#JUMP_SPEED = 5#
BOX_SCALING = 0.5
SPRITE_SCALING_BOX  = 0.1

class Kiwi(arcade.Sprite):
    def __init__(self, image):
        scaling_factor = 0.1

        super().__init__(image, scaling_factor)

    def update(self):
        if self.center_y > SCREEN_HEIGHT - 25:
            self.center_y = SCREEN_HEIGHT -25
        if self.center_y < 25:
            self.center_y = 25
        if self.center_x > SCREEN_WIDTH -25:
            self.center_x = SCREEN_WIDTH -25
        if self.center_x < 25:
            self.center_x = 25


class MenuScreen(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(RED)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("MENU" , SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, font_size = 50, anchor_x="center")
        arcade.draw_text("Click here to start...", SCREEN_WIDTH/2 + 10, SCREEN_HEIGHT/2 - 50, arcade.color.BLACK, font_size = 20, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GamePlay()
        game_view.setup()
        game_view.on_draw()
        self.window.show_view(game_view)

class GamePlay(arcade.View):

    def __init__(self):
        super().__init__()
        self.player_list = None
        self.wall_list = None  
        self.kiwi_sprite = None

        self.window.set_mouse_visible(False)
        self.kiwi_sprite = Kiwi('Images/kiwi_default.png')

        self.physics_engine = None


    
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        #create kiwi
        #self.kiwi_sprite = arcade.Sprite("Images/kiwi_default.png", 0.18)
        self.kiwi_sprite.center_x = SCREEN_WIDTH/2
        self.kiwi_sprite.center_y = SCREEN_HEIGHT/2

        self.player_list.append(self.kiwi_sprite)

       
        wall = arcade.Sprite("Images/box.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("Images/box.png", SPRITE_SCALING_BOX)
        wall.center_x = 450
        wall.center_y = 200
        self.wall_list.append(wall)

        for x in range(173, 650, 64):
            wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                          [470, 570]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.kiwi_sprite, self.wall_list)


        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()
        arcade.set_background_color(SKY_BLUE)
        arcade.draw_lrtb_rectangle_filled(0,799, 200, 0, GREEN)
        arcade.draw_lrtb_rectangle_filled(550,625,250,200, BLACK)
        self.kiwi_sprite.draw()

    
    def on_update(self, delta_time):
        self.kiwi_sprite.update()
        self.physics_engine.update()



        

        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.kiwi_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.kiwi_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.kiwi_sprite.right > right_boundary:
            self.view_left += self.kiwi_sprite.right - right_boundary
            changed = True

        

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.kiwi_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.kiwi_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.kiwi_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.kiwi_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.kiwi_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.kiwi_sprite.change_x = 0

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MenuScreen()
    window.show_view(start_view)
    arcade.run()

main()