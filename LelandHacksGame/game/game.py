import arcade
import numpy as np

# Constants(calculate based on screen size later?)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer test2"
GRAVITY = 1000
PLAYER_JUMP_SPEED = 12
# scale factors(fix later)
CHARACTER_SCALING = 32/27 * 1/2
PLAYER_MOVEMENT_SPEED = 5
TILE_SCALE = 1/2
TILE_SIZE = 64
PATH = r"C:\Users\ayush\OneDrive\Desktop\Leland Hacks Game\assets\\"
BLOCKS = PATH+r"images\blocks\\"
PLAYER_START_X = 4*TILE_SIZE
PLAYER_START_Y = 1.1*TILE_SIZE
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_DONT_TOUCH = "Don't Touch"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        self.level = 0
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.camera = None

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.title_map = None
        self.wall_list = None
        self.player_list = None

        self.scene = None
        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color((128, 128, 128))

        """Set up the game here. Call this function to restart the game."""

        self.scene = arcade.Scene()
        self.camera = arcade.Camera(self.width, self.height)
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()
        self.camera.use()
        # Draw our sprites
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                # arcade.play_sound(self.jump_sound)
                arcade.play_sound(arcade.load_sound(
                    r"C:\Users\ayush\OneDrive\Desktop\Leland Hacks Game\assets\sounds\cr.mp3"))
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.R:
            self.level0()
        elif key == arcade.key.T:
            self.level1()
        elif key == arcade.key.Z:
            if self.level == 0:
                self.level0()
                print("r")
                arcade.play_sound(arcade.load_sound(
                    r"C:\Users\ayush\OneDrive\Desktop\Leland Hacks Game\assets\sounds\oof.mp3"))

            else:
                self.level1()
                print("r")
                arcade.play_sound(arcade.load_sound(
                    r"C:\Users\ayush\OneDrive\Desktop\Leland Hacks Game\assets\sounds\oof.mp3"))

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()
        self.center_camera_to_player()
        if self.player_sprite.center_y < -5*TILE_SIZE:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y
            print("rip")
            if self.level == 0:
                self.level0()
                print("r")
                arcade.play_sound(arcade.load_sound(
                    r"C:\Users\ayush\OneDrive\Desktop\Leland Hacks Game\assets\sounds\oof.mp3"))

            else:
                self.level1()
                print("r")
                arcade.play_sound(arcade.load_sound(
                    r"C:\Users\ayush\OneDrive\Desktop\Leland Hacks Game\assets\sounds\oof.mp3"))
        if self.level == 0 and self.player_sprite.center_y >= 24*TILE_SIZE-16 and self.player_sprite.center_y <= 24*TILE_SIZE+16 and self.player_sprite.center_x >= 66*TILE_SIZE-16 and self.player_sprite.center_y <= 66*TILE_SIZE+16:
            self.level1()
            print("dgdff")
            self.level = 1

    def center_camera_to_player(self):

        screen_center_x = self.player_sprite.center_x - \
            (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 1.4
        )

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def level0(self):
        """Set up the game here. Call this function to restart the game."""

        self.scene = arcade.Scene()
        self.camera = arcade.Camera(self.width, self.height)
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)
        self.scene.add_sprite_list("Doors", use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite(
            PATH+r"images\player\player.png", CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite("Player", self.player_sprite)


# ------------------------------------
        coordinate_list = []
        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 8, 1):
            coordinate_list.append((x, 0))

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list += [

            (2, 2),
            (1, 3),
            (3, 5),
            (7, 7),
            (11, 7),
            (14, 6),
            (18, 6),
            (21, 7),
            (23, 9),
            (25, 11),
            (28, 13),
            (31, 13),
            (32, 13),
            (32, 22),
            (37, 13),
            (38, 13),
            (39, 14),
            (38, 16),
            (35, 18),
            (33, 20),
            (34, 23),
            (37, 24),
            (39, 26),
            (43, 26),
            (45, 24),
            (49, 24),
            (53, 23),
            (55, 22),
            (57, 19),
            (60, 20),
            (62, 22),
            (63, 23),
            (64, 23),
            (65, 23),
            (66, 23),
            (67, 23),
            (67, 24),
            (67, 25),
            (67, 26),
            (67, 27)
        ]

        for coordinate in np.multiply(coordinate_list, TILE_SIZE):
            # Add a crate on the ground
            wall = arcade.Sprite(BLOCKS+r"stone_wall_top.png", TILE_SCALE)
            wall.position = coordinate
            self.scene.add_sprite("Walls", wall)
        door = arcade.Sprite(BLOCKS+r"door.png", TILE_SCALE)
        door.position = (66*TILE_SIZE, 24*TILE_SIZE)
        self.scene.add_sprite("Doors", door)

    # -------------------------------------------

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.scene.get_sprite_list("Walls")
        )

    def level1(self):
        """Set up the game here. Call this function to restart the game."""
        arcade.play_sound(arcade.load_sound(
            r"C:\Users\ayush\OneDrive\Desktop\Leland Hacks Game\assets\sounds\amogus.mp3"))
        self.scene = arcade.Scene()
        self.camera = arcade.Camera(self.width, self.height)
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)
        self.scene.add_sprite_list("Doors", use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite(
            PATH+r"images\player\player.png", CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite("Player", self.player_sprite)

        stone_wall_top_list = []
        stone_wall_bottom_list = []
        stone_wall_left_list = []
        stone_wall_right_list = []
        stone_list = []

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(1, 19, 1):
            stone_wall_top_list.append((x, 0))

        # Create the ceiling
        for x in range(1, 19, 1):
            stone_wall_bottom_list.append((x, 9))

        # Create left wall
        for y in range(1, 9, 1):
            stone_wall_right_list.append((0, y))

        # Create right wall
        for y in range(1, 9, 1):
            stone_wall_left_list.append((20, y))

        # Create spikes
        spikes_list = [(6, 1), (9, 1)]

        # Create remaining stone outside of walls
        # above ceiling walls
        for x in range (-5, 26, TILE_SIZE):
           for y in range (12, 16, TILE_SIZE):
               stone_list.append((x,y))

        # below ground walls
        for x in range (-5, 26, TILE_SIZE):
            for y in range (-3, 2, TILE_SIZE):
                stone_list.append((x,y))

        # behind left walls
        for x in range (-5, -2, TILE_SIZE):
            for y in range (-1, 9, TILE_SIZE):
                stone_list.append((x,y))

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [

            #[TILE_SIZE*3, TILE_SIZE*4]
        ]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(BLOCKS+r"stone.png", TILE_SCALE)
            wall.position = coordinate
            self.scene.add_sprite("Walls", wall)

        for l in np.multiply(stone_wall_top_list, TILE_SIZE):
            block = arcade.Sprite(BLOCKS+r"stone_wall_top.png", TILE_SCALE)
            block.position = l
            self.scene.add_sprite("Walls", block)

        for l in np.multiply(stone_wall_bottom_list, TILE_SIZE):
            block = arcade.Sprite(BLOCKS+r"stone_wall_bottom.png", TILE_SCALE)
            block.position = l
            self.scene.add_sprite("Walls", block)

        for l in np.multiply(stone_wall_left_list, TILE_SIZE):
            block = arcade.Sprite(BLOCKS+r"stone_wall_left.png", TILE_SCALE)
            block.position = l
            self.scene.add_sprite("Walls", block)
        for l in np.multiply(stone_wall_right_list, TILE_SIZE):
            block = arcade.Sprite(BLOCKS+r"stone_wall_right.png", TILE_SCALE)
            block.position = l
            self.scene.add_sprite("Walls", block)
        block0 = arcade.Sprite(BLOCKS+r"spikes.png", .75)
        block0.position = (7*TILE_SIZE, 1*TILE_SIZE)
        self.scene.add_sprite("Walls", block0)
        block1 = arcade.Sprite(BLOCKS+r"troll.png", 2)
        for l in np.multiply(stone_wall_bottom_list, TILE_SIZE):
            block = arcade.Sprite(BLOCKS+r"stone_wall_bottom.png", TILE_SCALE)
            block.position = l
            self.scene.add_sprite("Walls", block)

        for l in np.multiply(stone_wall_left_list, TILE_SIZE):
            block = arcade.Sprite(BLOCKS+r"stone_wall_left.png", TILE_SCALE)
            block.position = l
            self.scene.add_sprite("Walls", block)
        block1.position = (2*TILE_SIZE, 4*TILE_SIZE)
        self.scene.add_sprite("Walls", block1)
        block2 = arcade.Sprite(BLOCKS+r"sanic.png", 2)
        block2.position = (12*TILE_SIZE, 2.5*TILE_SIZE)
        for l in np.multiply(stone_wall_right_list, TILE_SIZE):
            block = arcade.Sprite(BLOCKS+r"stone_wall_right.png", TILE_SCALE)
            block.position = l
        self.scene.add_sprite("Walls", block2)
        block3 = arcade.Sprite(BLOCKS+r"spoonge_bob.png", 2)
        block3.position = (15*TILE_SIZE, 1.5*TILE_SIZE)
        self.scene.add_sprite("Walls", block3)
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.scene.get_sprite_list("Walls"))


if __name__ == "__main__":
    window = MyGame()
    window.level0()
    arcade.run()
