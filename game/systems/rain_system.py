import arcade

from game.entities.rain_drop import RainDrop
from utils.game_utils import WINDOW_WIDTH, WINDOW_HEIGHT


class RainSystem:
    """Sistema que gerencia todas as gotas de chuva"""
    
    def __init__(self) -> None:
        """Inicializa o sistema de chuva com 1500 gotas"""
        self.rain_list: list[RainDrop] = []

        # Criar gotas
        for _ in range(1500):
            self.rain_list.append(RainDrop())
        
        self.rain_shapes = arcade.shape_list.ShapeElementList()

    def behaviour_update(self, delta_time: float, camera: arcade.Camera2D) -> None:
        """Atualiza posição de todas as gotas e renderiza"""
        # Pegar posição da câmera
        camera_x = camera.position[0]
        camera_y = camera.position[1]

        # Atualizar comportamento de cada gota
        for rain in self.rain_list:
            rain._behaviour(
                delta_time=delta_time,
                camera_x=camera_x,
                camera_y=camera_y,
                screen_width=WINDOW_WIDTH,
                screen_height=WINDOW_HEIGHT
            )
        
        # Reconstruir lista de formas para renderização
        self.rain_shapes = arcade.shape_list.ShapeElementList()
        for rain in self.rain_list:
            self.rain_shapes.append(rain.get_shape())