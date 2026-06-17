import random
import arcade

class RainDrop:
    """Representa uma gota de chuva"""
    
    def __init__(self) -> None:
        # Posição inicial aleatória
        self.x = random.randint(0, 1600)
        self.y = random.randint(0, 900)
        self.speed = random.randint(500, 900)  # pixels/seg
        self.line_width = random.randint(1, 3)

    def _behaviour(self, delta_time: float, camera_x: float, camera_y: float, screen_width: int, screen_height: int) -> None:
        """Atualiza posição da gota de chuva"""
        # Chuva cai para baixo
        self.y -= self.speed * delta_time

        # Limites da câmera (com margem extra para spawnar fora da tela)
        left = camera_x - screen_width / 2 - 1200
        right = camera_x + screen_width / 2 + 1200
        bottom = camera_y - screen_height / 2 - 200
        top = camera_y + screen_height / 2 + 200

        # Se a gota saiu do fundo, volta ao topo com novo X aleatório
        if self.y < bottom:
            self.y = top
            self.x = random.uniform(left, right)
    
    def get_shape(self):
        """Retorna a gota como uma linha do arcade"""
        return arcade.shape_list.create_line(
            start_x=self.x,
            start_y=self.y,
            end_x=self.x + 6,
            end_y=self.y - 20,
            color=arcade.color.BLUE_GRAY,
            line_width=self.line_width
        )