from game.entities.towels import Towels
from game.core.config import TowelsConfig
import arcade


class TowelsSceneManager:
    def __init__(self, window: arcade.Window) -> None:
        self.towels: dict[str, Towels] = {}
        self._spawned = False

        for towels_name, config in TowelsConfig.TOWELS.items():
            towels = Towels(
                path=config["path"],
                x=config["x"],
                y=config["y"],
                window=window
            )
            self.towels[towels_name] = towels

    def __getattr__(self, name: str) -> Towels:
        towels = self.__dict__.get("towels", {})
        if name in towels:
            return towels[name]
        raise AttributeError(f"Toalha '{name}' não encontrada.")

    def on_spawn(self, sprite_list: arcade.SpriteList, physics_engine) -> None:
        if self._spawned:
            return
        for towels in self.towels.values():
            towels.on_spawn(sprite_list, physics_engine)
        self._spawned = True

    def check_triggers(self, sprite_list: arcade.SpriteList) -> None:
        for towel in self.towels.values():
            towel.check_trigger(sprite_list)