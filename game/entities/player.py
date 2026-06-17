from game.core import GameObject, PlayerConfig

import arcade

class Player(GameObject):
    
    def __init__(self) -> None:
        super().__init__()

        self.left_pressed = False
        self.right_pressed = False
        self.jumped = False

        self.is_running = False
        self.facing_right = False

        self.center_x = PlayerConfig.START_X
        #self.center_x = -10000
        self.center_y = PlayerConfig.START_Y

        self.scale = 1.0
        self.scale_x = 1

    def on_spawn(self, sprite_list: arcade.SpriteList, physics_engine) -> None:
        """Adiciona o player à lista de sprites e configura o motor de física"""
        sprite_list.append(self)
        self.physics_engine = physics_engine
    