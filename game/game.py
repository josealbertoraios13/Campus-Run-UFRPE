from utils import WINDOW_WIDTH, WINDOW_HEIGHT
from game.views.game_manager import GameManager
from pathlib import Path
import arcade

class Game(arcade.View):

    def __init__(self) -> None:
        super().__init__()

        font_path = Path("assets/font/Jersey10-Regular.ttf")
        arcade.load_font(font_path)

        menu_image_path = Path("assets/images/main_menu.png")
        self.background = arcade.load_texture(menu_image_path)


        self.title = arcade.Text(
            text="Campus Run UFRPE",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT / 2 + 200,
            color=arcade.color.WHITE,
            font_size=82,
            font_name="Jersey 10",
            anchor_x="center",
        )

        self.press_enter = arcade.Text(
            text="Press ENTER to start",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT / 2 - 120,
            color=arcade.color.WHITE,
            font_size=20,
            font_name="Jersey 10",
            anchor_x="center")
    
    def on_draw(self) -> bool | None:

        arcade.draw_texture_rect(
            texture=self.background,
            rect=arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        self.title.draw()
        self.press_enter.draw()

    def on_update(self, delta_time: float) -> bool | None:
        return super().on_update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        if symbol == arcade.key.ENTER:
            in_game = GameManager()
            self.window.show_view(in_game)