from game.core.config import GameConfig
import arcade

class HudSystem:
    def __init__(self) -> None:
        self.towels = 0
        self.wetness_level = 0
        self.time_elapsed = 0.0

        self.pos_y = GameConfig.WINDOW_HEIGHT - 50

        self.icons = arcade.SpriteList()

        self.wetness_icon = arcade.Sprite("assets/images/wetness.png", 0.07)
        self.towel_icon = arcade.Sprite("assets/images/towels.png", 0.07)
        self.time_icon = arcade.Sprite("assets/images/clock.png", 0.07)

        self.icons.append(self.wetness_icon)
        self.icons.append(self.towel_icon)
        self.icons.append(self.time_icon)

    def add_wetness(self, amount: float) -> None:
        self.wetness_level = min(100, self.wetness_level + amount)

    def remove_wetness(self, amount: float) -> None:
        self.wetness_level = max(0, self.wetness_level - amount)

    def update(self, delta_time: float) -> None:
        self.add_wetness(0.25)
        self.time_elapsed += delta_time

    def draw(self) -> None:
        minutes = int(self.time_elapsed // 60)
        seconds = int(self.time_elapsed % 60)

        self.wetness_icon.position = (20, self.pos_y + 12)

        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                x=155,
                y=self.pos_y + 12,
                width=204,
                height=24
            ),
            arcade.color.DARK_GRAY
        )

        bar_width = (self.wetness_level / 100) * 204
        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                x=53 + bar_width / 2,  
                y=self.pos_y + 12,
                width=bar_width,
                height=20
            ),
            arcade.color.BLUE
        )

        arcade.draw_text(
            text=f"{int(self.wetness_level)}%",
            x=50,
            y=self.pos_y - 20,
            color=arcade.color.WHITE,
            font_size=16
        )

        self.towel_icon.position = (300, self.pos_y + 12)

        arcade.draw_text(
            text=f"{self.towels}",
            x=350,
            y=self.pos_y,
            color=arcade.color.WHITE,
            font_size=20
        )

        self.time_icon.position = (420, self.pos_y + 12)

        arcade.draw_text(
            text=f"{minutes:02d}:{seconds:02d}",
            x=460,
            y=self.pos_y,
            color=arcade.color.WHITE,
            font_size=20
        )

        self.icons.draw()
