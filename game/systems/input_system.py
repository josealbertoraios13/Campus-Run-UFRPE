from game.core import InputHandler
from game.entities import Player

import arcade

class InputSystem(InputHandler):
    def __init__(self, player: Player) -> None:
        self.player = player

    def on_key_press(self, symbol: int) -> None:
        if symbol in (arcade.key.RIGHT,  arcade.key.D):
            self.player.right_pressed = True
        
        elif symbol in (arcade.key.LEFT, arcade.key.A):
            self.player.left_pressed = True

        elif symbol == arcade.key.SPACE:
            self.player.jumped = True

    def on_key_release(self, symbol: int) -> None:
        if symbol in (arcade.key.RIGHT,  arcade.key.D):
            self.player.right_pressed = False
        
        elif symbol in (arcade.key.LEFT, arcade.key.A):
            self.player.left_pressed = False

        elif symbol == arcade.key.SPACE:
            self.player.jumped = False