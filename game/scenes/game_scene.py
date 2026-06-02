from systems import InputSystem
from entities import Player

import arcade

class GameScene(arcade.View):
    def __init__(self) -> None:
        super().__init__()

        self.player = Player() 
        self.input_system = InputSystem(player=self.player)

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        self.input_system.on_key_press(symbol=symbol)

    def on_key_release(self, symbol: int, modifiers: int) -> bool | None:
        self.input_system.on_key_release(symbol=symbol)