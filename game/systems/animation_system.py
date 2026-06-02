from core import System, PlayerConfig
from entities import Player

import arcade

class AnimationSystem(System):
    def __init__(self, player: Player) -> None:
        self.player = player
        self.animation_timer = 0
        self.current_frame = 0

        self._load_sprites()

    def _load_sprites(self) -> None:
        self.idle_sheet = arcade.load_spritesheet(PlayerConfig.IDLE_SPRITE)
        self.run_sheet = arcade.load_spritesheet(PlayerConfig.RUN_SPRITE)

        self.idle_frames = self.idle_sheet.get_image_grid(
            size=PlayerConfig.SPRITE_SIZE,
            columns=PlayerConfig.SPRITE_COLUMNS,
            count=PlayerConfig.IDLE_FRAME_COUNT
        )

        self.run_frames = self.run_sheet.get_image_grid(
            size=PlayerConfig.SPRITE_SIZE,
            columns=PlayerConfig.SPRITE_COLUMNS,
            count=PlayerConfig.RUN_FRAME_COUNT
        )

    def update(self, delta_time: float) -> None:
        if self.player.is_running:
            self._update_run_animation(delta_time=delta_time)
        else:
            self._update_idle_animation(delta_time=delta_time)

    def _update_idle_animation(self, delta_time: float) -> None:
        self.animation_timer += delta_time

        if self.animation_timer >= PlayerConfig.IDLE_FRAME_RATE:
            self.animation_timer = 0

            self.cur_texture += 1

            if self.cur_texture >= len(self.idle_frames):
                self.cur_texture = 0

            self.texture = arcade.Texture(
                image=self.idle_frames[self.cur_texture]
            )

    def _update_run_animation(self, delta_time: float) -> None:
        self.animation_timer += delta_time

        if self.animation_timer >= PlayerConfig.RUN_FRAME_RATE:
            self.animation_timer = 0
            
            self.cur_texture += 1

            if self.cur_texture >= len(self.run_frames):
                self.cur_texture = 0

            self.texture = arcade.Texture(
                image=self.run_frames[self.cur_texture]
            )

    def reset(self) -> None:
        # Resetar animação (usado na mudança de estados)
        self.animation_timer = 0
        self.current_frame = 0