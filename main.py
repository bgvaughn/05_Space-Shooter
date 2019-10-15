#!/usr/local/env python3
import sys, logging, os, open_color, arcade, assets

version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "The Space Between Us!"
MARGIN = 50

SHIP_HP = 100
SHIP_SCALE = 0.5

NUM_ENEMIES = 5
ENEMY_SCALE = 0.5
ENEMY_MIN_Y = 400
ENEMY_MIN_HP = 10
ENEMY_MAX_HP = 50
ENEMY_MIN_MASS = 10
ENEMY_MAX_MASS = 100
ENEMY_ACCELERATION = 10


class Player(arcade.Sprite):
    def __init__(self, image, scale, x, y):
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.dx = 0
        self.dy = 0
        self.target_x = x
        self.target_y = y

class Enemy(arcade.Sprite):
    def __init__(self, x, y, mass, hp):
        sprites = ['enemy_01', 'enemy_02', 'enemy_03', 'enemy_04', 'enemy_05', 'enemy_06', 'enemy_07', 'enemy_08', 'enemy_09']
        sprites = random.choice(sprites)
        super().__init__("assets/{}.png".format(sprite), ENEMY_SCALE)
        self.center_x = x
        self.center_y = y
        self.hp = hp
        self.mass = mass
        self.dx = 0
        self.dy = 0
        self.target_x = x
        self.target_y = y
        self.acceleration =ENEMY_ACCELERATION / self.mass

class Window(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.set_mouse_visible(True)

        arcade.set_background_color(open_color.blue_4)

        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()



    def setup(self):
        self.player = True
        self.score = 0.0
        self.hp = SHIP_HP
        

        self.player = Player("assets/player.png", SHIP_SCALE,400,50)
        self.player_list.append(self.player)
        for e in range(NUM_ENEMIES):
            x = random.randint(MARGIN,SCREEN_WIDTH-MARGIN)
            y = random.randint(SCREEN_HEIGHT-ENEMY_MIN_Y,SCREEN_HEIGHT-MARGIN)
            hp = random.randint(ENEMY_MIN_HP,ENEMY_MAX_HP)
            mass = random.randint(ENEMY_MIN_MASS,ENEMY_MAX_MASS)
            enemy = Enemy(x, y, mass, hp)
            self.enemy_List.append(enemy)

    def update(self, delta_time):
        pass

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.enemy_bullet_list.draw()




    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            print("Left")
        elif key == arcade.key.RIGHT:
            print("Right")
        elif key == arcade.key.UP:
            print("Up")
        elif key == arcade.key.DOWN:
            print("Down")

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        pass


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()