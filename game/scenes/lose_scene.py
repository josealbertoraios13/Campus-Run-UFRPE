from game.core import VisualConfig, GameConfig
from pathlib import Path
import arcade

class LoseScene(arcade.View):
    def __init__(self) -> None:
        super().__init__()

        self.background_color = VisualConfig.BACKGROUND_COLOR
        
        font_path = Path(VisualConfig.FONT_PATH)
        arcade.load_font(font_path)
        
        menu_image_path = Path(VisualConfig.LOSE_IMAGE)
        self.background = arcade.load_texture(str(menu_image_path))
        
        self.title = arcade.Text(
            text="VOCÊ PERDEU!!",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 + 200,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_TITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center",
        )
        
        self.lose_text = arcade.Text(
            text="Você ficou totalmente encharcado",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 - 60,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_SUBTITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center",
        )

        self.guide_text = arcade.Text(
            text="Colete as toalhas para que você consigar chegar minimamente enxuto",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 - 120,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_SUBTITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center",
        )

        self.instructions = arcade.Text(
            text="Pressione ENTER para voltar ao menu",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 - 260,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_SUBTITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center",
        )
    
    def on_draw(self) -> None:
        self.clear()
        
        arcade.draw_texture_rect(
            texture=self.background,
            rect=arcade.LBWH(0, 0, GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT)
        )

        self.title.draw()
        self.lose_text.draw()
        self.guide_text.draw()
        self.instructions.draw()
    
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.ENTER:
            self.window.scene_manager.switch_to_menu()  # type: ignore
