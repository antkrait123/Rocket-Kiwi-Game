#imports
import arcade
from arcade.color import BLACK, GREEN, RED, SKY_BLUE, YELLOW
import random
import math

# Constants
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = "ROCKET KIWI"
MOVEMENT_SPEED = 8
BULLET_SPEED = 10


#background_images = []

#SPRITE_SCALING_BOX  = 0.1
#SPRITE_SCALING_CABBAGETREE = 0.2
#SPRITE_SCALING_NIKAUTREE = 0.25
#SPRITE_SCAING_ROCK = 0.15
#SPRITE_SCALING_SMALLROCK = 0.1

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
        
class Cloud:
    def __init__(self, center_x, center_y, size):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        self.speed = self.size / 20

    def update(self):
        self.center_x -= self.speed
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.size, arcade.color.WHITE)
        arcade.draw_circle_filled(self.center_x-self.size, self.center_y, self.size, arcade.color.WHITE)
        arcade.draw_circle_filled(self.center_x+self.size, self.center_y, self.size, arcade.color.WHITE)
        arcade.draw_circle_filled(self.center_x -self.size/3, self.center_y + self.size/1.5, self.size, arcade.color.WHITE)


class MenuScreen(arcade.View):
    def __init__(self):
        super().__init__()
        #self.music_sound = arcade.load_sound("")
        

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
        #arcade.play_sound(self.music_sound)




class GamePlay(arcade.View):

    def __init__(self):
        super().__init__()
        self.player_list = None
        self.enemy_list = None
        self.wall_list = None  
        self.bullet_list = None
        self.kiwi_sprite = None
        self.physics_engine = None
        self.window.set_mouse_visible(False)
        self.kiwi_sprite = Kiwi('Images/rocket_kiwi.png')
        self.score = None
        self.gspeed = None
        self.background_sprites = None
        self.backgroundsky_sprites = None
        self.clouds = []
        self.num_possums = 3
        for i in range(10):
            self.make_cloud()

        #load sounds & tunes
        self.shoot_sound = arcade.load_sound("Sounds/pop.mp3")
        self.endgame_noise = arcade.load_sound("Sounds/Game_over_sound.mp3")
        #self.crash_sound = arcade.load_sound("")

          
    def setup(self):
        #arcade.draw_text("Use arrow keys to move < ^ >" , 100, 600, arcade.color.BLACK, font_size = 20, anchor_x="center")
        #arcade.draw_text("Use [SPACE] to shoot", 100, 550, arcade.color.BLACK, font_size = 20, anchor_x="center")
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.kiwi_sprite.center_x = SCREEN_WIDTH/2
        self.kiwi_sprite.center_y = SCREEN_HEIGHT/2

        self.player_list.append(self.kiwi_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.kiwi_sprite, self.wall_list)

        self.background_sprites = arcade.SpriteList()
        self.backgroundsky_sprites = arcade.SpriteList()

        self.score = 0
        self.gspeed = 3
        

        #place boxes continually in sequence
        for x in range(0, 1080, 100):
            wall = arcade.Sprite("images/piskelbox.png", 0.07)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        self.spawn_possum()
        self.spawn_possum()
        self.spawn_possum()


        #manualy place a tree
        '''tree = arcade.Sprite("images/Nikau_tree.png", 0.2)
        tree.center_x = 100
        tree.center_y = 200
        self.background_sprites.append(tree)'''

        sun = arcade.Sprite("images/sun.png", 0.06)
        sun.center_x = 980
        sun.center_y = 600
        self.background_sprites.append(sun)

        # for x in range(-100, 1100, random.randint(50, 200)):
        #     cloudsprites = ["images/cloud1.png",
        #     "images/cloud2.png",
        #     "images/cloud3.png"]
        #     clouds = arcade.Sprite(random.choice(cloudsprites), random.uniform(0.1, 0.25))
        #     clouds.center_x = x
        #     clouds.center_y = random.randint(400, SCREEN_HEIGHT)
        #     self.background_sprites.append(clouds)


        #give users instructions
        '''instructions = arcade.draw_text("Use arrow keys to move < ^ >" , 100, 600, arcade.color.BLACK, font_size = 30, anchor_x="center")
        instructions.center_x = 1000
        instructions. center_y = 650
        self.wall_list.append(instructions)

        instructions2 = arcade.draw_text("Use [SPACE] to shoot" , 100, 600, arcade.color.BLACK, font_size = 30, anchor_x="center")
        instructions2.center_x = 1000
        instructions2. center_y = 590
        self.wall_list.append(instructions2)'''
        
       

        # place boxes at specified co-ordinates   
    ''' coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                          [470, 570]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)'''


    '''def make_l_shape(self, x, y):
        box_size = 51.2
        wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
        wall.center_x = x
        wall.center_y = y
        self.wall_list.append(wall)
        wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
        wall.center_x = x + box_size
        wall.center_y = y
        self.wall_list.append(wall)
        for i in range(5):
            wall = arcade.Sprite("images/box.png", SPRITE_SCALING_BOX)
            wall.center_x = x + box_size * 2
            wall.center_y = y + box_size * i
            self.wall_list.append(wall) '''


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0 ,1080, 200, 0, GREEN)
        self.background_sprites.draw()
        for cloud in self.clouds:
            cloud.draw()
        #arcade.draw_lrtb_rectangle_filled(300, 350, 200, 150, BLACK)
        self.wall_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        arcade.set_background_color(SKY_BLUE)
        self.kiwi_sprite.draw()
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 50, arcade.color.BLACK, font_size = 35 )


    def make_cloud(self):
        cloud = Cloud(random.randint(SCREEN_WIDTH, 2*SCREEN_WIDTH), random.randint(2*SCREEN_HEIGHT/3, SCREEN_HEIGHT), random.randint(15, 50))
        self.clouds.append(cloud)

    def spawn_possum(self):
        enemy = arcade.Sprite("images/possum.png", 0.33)
        enemy.center_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH*3)
        enemy.center_y = random.randint(0, SCREEN_HEIGHT)
        self.enemy_list.append(enemy)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.kiwi_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.kiwi_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.kiwi_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.kiwi_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            arcade.play_sound(self.shoot_sound)
            bullet = arcade.Sprite("images/pellet.png", 0.0075)
            start_x = self.kiwi_sprite.center_x + 25
            start_y = self.kiwi_sprite.center_y + 10
            bullet.center_x = start_x
            bullet.center_y = start_y
            bullet.change_x =  BULLET_SPEED
            self.bullet_list.append(bullet)



    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.kiwi_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.kiwi_sprite.change_x = 0



    def on_update(self, delta_time):
        self.kiwi_sprite.update()
        self.physics_engine.update()
        self.bullet_list.update()
        self.enemy_list.update()
        self.background_sprites.update()
        for cloud in self.clouds:
            cloud.update()
            if cloud.center_x < -100:
                self.clouds.remove(cloud)
                self.make_cloud()


        for sun in self.background_sprites:
            sun.center_x -= (0.15)
        if sun.center_x == -40:
            moon.draw()
            moon.center_x -=(0.15)


        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for enemy in hit_list:
                    enemy.kill()
                    chance = random.random()
                    self.spawn_possum()
                    self.score += 10
                
            if bullet.center_x > SCREEN_WIDTH - 10 or bullet.center_y > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
            
        '''for wall in self.wall_list:
            wall.center_x -= 5
            shape_chance = random.random()
            if shape_chance < 0.05:
                self.make_l_shape(850, random.randint(0, SCREEN_HEIGHT))
            else: '''

        for wall in self.wall_list:
            wall.center_x -= (self.gspeed)
            if wall.center_x < -50:
                wall.kill()
                sprites = ["images/piskelbox.png" ] 
                #"images/Nikau_tree.png", 
                #"images/cabbage_tree.png", 
                #"images/rock.png", 
                #"images/small_rock.png"]
                new_wall = arcade.Sprite(random.choice(sprites), 0.07)
                new_wall.center_x = 1300
                new_wall.center_y = random.randint(0, SCREEN_HEIGHT)
                self.wall_list.append(new_wall)
                self.score += 1
        
        '''for background in self.background_sprites:
            background.center_x -= (self.gspeed)
            if  background.center_x < -50:
                background.kill()
                sprites = [" images/Nikau_tree.png", 
                "images/cabbage_tree.png", 
                "images/rock.png", 
                "images/small_rock.png"]
                new_background = arcade.Sprite(random.choice(sprites), 0.1)
                new_background.center_x = 1500
                new_background.center_y = random.randint(10, 150)
                self.background_sprites.append(new_background)'''


        for enemy in self.enemy_list:
            enemy.center_x -= (self.gspeed)
            # enemy.center_y = arcade.utils.lerp(enemy.center_y, self.kiwi_sprite.center_y, 0.02) 
            if enemy.center_x < -50:
                enemy.kill()
                self.spawn_possum()
        
        enemy_hit_list = arcade.check_for_collision_with_list(self.kiwi_sprite, self.enemy_list)
        for enemy in enemy_hit_list:
            self.game_over()

        if self.kiwi_sprite.center_x < -20:
            self.game_over()

        self.num_possums = math.floor(self.score/100) + 3
        while len(self.enemy_list) < self.num_possums:
            self.spawn_possum()

        self.gspeed += delta_time/10
        print(self.gspeed)

    
    def game_over(self):
        arcade.play_sound(self.endgame_noise)
        arcade.get_window().show_view(EndScreen(self.score))




class EndScreen(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.score = score
    
    def on_show(self):
        arcade.set_background_color(RED)
        self.window.set_mouse_visible(True)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER!" , SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, font_size = 75, anchor_x="center")
        arcade.draw_text(f"Your Score: {self.score} ", SCREEN_WIDTH/2 + 10, SCREEN_HEIGHT/2 - 75, arcade.color.BLACK, font_size = 50, anchor_x="center")
        arcade.draw_text("Click here to play again...", SCREEN_WIDTH/2 + 10, SCREEN_HEIGHT/2 - 120, arcade.color.BLACK, font_size = 20, anchor_x="center")
    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GamePlay()
        game_view.setup()
        game_view.on_draw()
        self.window.show_view(game_view)

 

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MenuScreen()
    window.show_view(start_view)
    arcade.run()

main()