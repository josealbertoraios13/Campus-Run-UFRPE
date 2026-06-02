import random
import arcade

class RainDrop:
    def __init__(self) -> None:
        self.x = random.randint(0, 1600)
        self.y = random.randint(0, 900)
        self.speed = random.randint(500, 900)
        self.line_width = random.randint(1, 3)

    def _behaviour(self, delta_time: float, camera_x: float, camera_y: float, screen_width: int, screen_height: int) -> None:
        self.y -= self.speed * delta_time

        left = camera_x - screen_width / 2
        right = camera_x + screen_width / 2

        bottom = (camera_y - 200) - screen_height / 2
        top = camera_y + screen_height / 2

        if self.y < bottom:
            self.y = top
            self.x = random.randint(
                int(left - 800),
                int(right + 800)
            )
    
    def get_shape(self):
        return arcade.shape_list.create_line(
            start_x=self.x,
            start_y=self.y,
            end_x=self.x + 6,
            end_y=self.y - 20,
            color=arcade.color.BLUE_GRAY,
            line_width=self.line_width
        )