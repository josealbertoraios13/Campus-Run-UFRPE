"""
Sistema da Camera
"""

from game.core import System
from game.core import CameraConfig

from game.entities import Player

import arcade

class CameraSystem(System):
    def __init__(self, camera: arcade.Camera2D, player: Player) -> None:
        self.player = player
        self.camera = camera
        self._initialize_camera()

    def _initialize_camera(self) -> None:
        self.camera.zoom = CameraConfig.ZOOM

    def update(self, delta_time: float) -> None:
        current_position = arcade.Vec2(
            self.camera.position[0],
            self.camera.position[1]
        )

        target_position = arcade.Vec2(
            self.player.position[0],
            self.player.position[1] + CameraConfig.OFFSET_Y
        )

        new_position = arcade.math.lerp_2d(
            current_position, 
            target_position,
            CameraConfig.LERP_FACTOR
        )

        self.camera.position = new_position