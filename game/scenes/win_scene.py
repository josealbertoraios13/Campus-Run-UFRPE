from game.core import VisualConfig, GameConfig
from pathlib import Path
import arcade

class WinScene(arcade.View):
    def __init__(self, status) -> None:
        super().__init__()
        self.status = status

        self.background_color = VisualConfig.BACKGROUND_COLOR
        
        font_path = Path(VisualConfig.FONT_PATH)
        arcade.load_font(font_path)
        
        menu_image_path = Path(VisualConfig.WIN_IMAGE)
        self.background = arcade.load_texture(str(menu_image_path))
        
        self.title = arcade.Text(
            text="VOCÊ VENCEU!!",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 + 200,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_TITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center",
        )
        
        self.towels_text = arcade.Text(
            text=f"Toalhas coletadas: {status['towels']}",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 - 60,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_SUBTITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center",
        )

        self.wet_text = arcade.Text(
            text=f"Nível de molhado: {status['wet_level']}%",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 - 120,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_SUBTITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center",
        )

        self.time_text = arcade.Text(
            text=f"Tempo: {status['time']:.2f}s",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 - 180,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_SUBTITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center",
        )

        self.instructions = arcade.Text(
            text="Pressione ESPAÇO para voltar ao menu",
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
        self.towels_text.draw()
        self.wet_text.draw()
        self.time_text.draw()
        self.instructions.draw()
    
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.SPACE:
            self.window.scene_manager.switch_to_menu()  # type: ignore
