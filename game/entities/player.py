import arcade



class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.idle_sheet = arcade.load_spritesheet(
            "assets/sprites/player/beto-idle.png"
        )

        self.run_sheet = arcade.load_spritesheet(
            "assets/sprites/player/beto-run.png"
        )

        self.idle_frames = self.idle_sheet.get_image_grid(
            size=(256, 256),
            columns=5,
            count=25
        )

        self.run_frames = self.run_sheet.get_image_grid(
            size=(256,256),
            columns=5,
            count=25
        )

        self.left_pressed = False
        self.right_pressed = False
        self.jumped = False

        self.cur_texture = 0
        self.animation_timer = 0

        self.is_running = False
        self.facing_right = True

    def start(self, player_list: arcade.SpriteList, physics_engine: arcade.PhysicsEnginePlatformer) -> None:
        player_list.append(self)        
        self.center_x = 800
        self.center_y = 200

        self.left_pressed = False
        self.right_pressed = False
        self.jumped = False

        self.physics_engine = physics_engine

