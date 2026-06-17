from game.core import VisualConfig, GameConfig
from pathlib import Path
import arcade

class MenuScene(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        self.background_color = VisualConfig.BACKGROUND_COLOR
        
        # Load font
        font_path = Path(VisualConfig.FONT_PATH)
        arcade.load_font(font_path)
        
        # Load background image
        menu_image_path = Path(VisualConfig.MENU_IMAGE)
        self.background = arcade.load_texture(str(menu_image_path))
        
        # Create title text
        self.title = arcade.Text(
            text="Campus Run UFRPE",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 + 200,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_TITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center",
        )
        
        # Create instructions text
        self.instructions = arcade.Text(
            text="Aperte ENTER para começar",
            x=GameConfig.WINDOW_WIDTH // 2,
            y=GameConfig.WINDOW_HEIGHT // 2 - 120,
            color=arcade.color.WHITE,
            font_size=VisualConfig.MENU_SUBTITLE_SIZE,
            font_name=VisualConfig.FONT_NAME,
            anchor_x="center"
        )
    
    def on_draw(self) -> None:
        self.clear()
        
        # Draw background image
        arcade.draw_texture_rect(
            texture=self.background,
            rect=arcade.LBWH(0, 0, GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT)
        )
        
        # Draw texts
        self.title.draw()
        self.instructions.draw()
    
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.ENTER:
            self.window.scene_manager.switch_to_game()  # type: ignore
        elif symbol == arcade.key.ESCAPE:
            self.window.close()
