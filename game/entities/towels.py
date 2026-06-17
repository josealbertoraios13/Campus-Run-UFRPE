from game.core.base import TriggerObject
from game.entities import Player
import arcade


class Towels(TriggerObject):
    def __init__(self, path: str, x: float, y: float, window: arcade.Window) -> None:
        super().__init__()
        self.game_window = window
        self.texture = arcade.load_texture(path)
        self.center_x = x
        self.center_y = y
        self.scale = 0.1
        
        self.triggered = False

    def on_trigger(self, other) -> None:
        if isinstance(other, Player) and not self.triggered:
            self.triggered = True
            game_scene = self.game_window.scene_manager.game_scene # type: ignore

            game_scene.hud.add_towels()

            self.remove_from_sprite_lists()

    def on_spawn(self, sprite_list: arcade.SpriteList, physics_engine) -> None:
        sprite_list.append(self)