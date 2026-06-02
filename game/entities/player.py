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

    def update_animation(self, delta_time: float):
        if self.is_running:
            self._run_animation(delta_time=delta_time)
        else:
            self._idle_animation(delta_time=delta_time)

    def _idle_animation(self, delta_time: float) -> None:
        self.animation_timer += delta_time

        if self.animation_timer >= 0.07:
            self.animation_timer = 0

            self.cur_texture += 1

            if self.cur_texture >= len(self.idle_frames):
                self.cur_texture = 0

            self.texture = arcade.Texture(
                image=self.idle_frames[self.cur_texture]
            )

    def _run_animation(self, delta_time: float) -> None:
        self.animation_timer += delta_time

        if self.animation_timer >= 0.05:
            self.animation_timer = 0
            
            self.cur_texture += 1

            if self.cur_texture >= len(self.run_frames):
                self.cur_texture = 0

            self.texture = arcade.Texture(
                image=self.run_frames[self.cur_texture]
            )