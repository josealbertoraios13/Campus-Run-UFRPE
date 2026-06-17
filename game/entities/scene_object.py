from game.core import GameObject

import arcade

class SceneObject(GameObject):
    def __init__(self, path: str, x: float, y: float) -> None:
        super().__init__()

        self.texture = arcade.load_texture(path)
        self.center_x = x
        self.center_y = y

    def on_spawn(self, sprite_list : arcade.SpriteList, physics_engine) -> None:
        """Adiciona o objeto de cena à lista de sprites"""
        sprite_list.append(self)