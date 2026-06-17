from abc import ABC, ABCMeta, abstractmethod

import arcade

class System(ABC):
    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

class GameObjectMeta(ABCMeta, type(arcade.Sprite)):
    pass

class GameObject(arcade.Sprite, metaclass=GameObjectMeta):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def on_spawn(self, sprite_list, physics_engine) -> None:
        pass


class TriggerObject(GameObject):
    
    def __init__(self) -> None:
        super().__init__()

    def on_trigger(self, other) -> None:
        raise NotImplementedError("Subclasses devem implementar on_trigger()")

    def check_trigger(self, sprite_list: arcade.SpriteList):
        collided = arcade.check_for_collision_with_list(self, sprite_list=sprite_list)
        for sprite in collided:
            if sprite is not self:
                self.on_trigger(sprite)

    def on_spawn(self, sprite_list: arcade.SpriteList, physics_engine) -> None:
        sprite_list.append(self)


class InputHandler(ABC):
    @abstractmethod
    def on_key_press(self, symbol: int) -> None:
        pass

    @abstractmethod
    def on_key_release(self, symbol: int) -> None:
        pass