"""
Classes bases e abstratas
"""

from abc import ABC, abstractmethod

import arcade

class System(ABC):
    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

class GameObject(arcade.Sprite):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def on_spawn(self) -> None:
        # Quando o objeto é instanciado
        pass

    @abstractmethod
    def on_update(self, delta_time: float) -> None:
        # A cada frame
        pass

    @abstractmethod
    def on_destroy(self) -> None:
        # Quando o objeto é destruído
        pass

class InputHandler(ABC):
    @abstractmethod
    def on_key_press(self, symbol: int) -> None:
        pass

    def on_key_release(self, symbol: int) -> None:
        pass