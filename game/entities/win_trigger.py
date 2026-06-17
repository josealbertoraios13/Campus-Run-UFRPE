from game.core import TriggerObject
from game.entities import Player
import arcade

class WinTrigger(TriggerObject):
    def __init__(self, window: arcade.Window):
        super().__init__()
        self.game_window = window

        self.width = 250
        self.height = 400

        self.center_x = -9700
        self.center_y = 390

        self.triggered = False

    def on_spawn(self, sprite_list: arcade.SpriteList, physics_engine) -> None:
        self.texture = arcade.make_soft_square_texture(
            size=250,
            color=arcade.color.GREEN,
            outer_alpha=10
        )

        super().on_spawn(sprite_list, physics_engine)

    def on_trigger(self, other):
        if isinstance(other, Player) and not self.triggered:
            self.triggered = True

            game_scene = self.game_window.scene_manager.game_scene # type: ignore
            status = {
                "towels": game_scene.hud.towels,
                "wet_level": game_scene.hud.wetness_level,
                "time": game_scene.hud.time_elapsed,
            }
            self.game_window.scene_manager.switch_to_win(status)  # type: ignore