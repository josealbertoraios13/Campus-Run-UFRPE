import arcade

from game.entities.rain_drop import RainDrop
from game.core.config import GameConfig


class RainSystem:
    
    def __init__(self) -> None:
        self.rain_list: list[RainDrop] = []

        for _ in range(1500):
            self.rain_list.append(RainDrop())
        
        self.rain_shapes = arcade.shape_list.ShapeElementList()

    def behaviour_update(self, delta_time: float, camera: arcade.Camera2D) -> None:
        camera_x = camera.position[0]
        camera_y = camera.position[1]

        for rain in self.rain_list:
            rain._behaviour(
                delta_time=delta_time,
                camera_x=camera_x,
                camera_y=camera_y,
                screen_width=GameConfig.WINDOW_WIDTH,
                screen_height=GameConfig.WINDOW_HEIGHT
            )
        
        self.rain_shapes = arcade.shape_list.ShapeElementList()
        for rain in self.rain_list:
            self.rain_shapes.append(rain.get_shape())