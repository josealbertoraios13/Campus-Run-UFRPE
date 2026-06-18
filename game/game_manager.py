from game.scenes.scene_manager import SceneManager
from game.core import WindowConfig
import arcade

class GameManager(arcade.Window):
    def __init__(self) -> None:
        super().__init__(
            width=WindowConfig.WINDOW_WIDTH,
            height=WindowConfig.WINDOW_HEIGHT,
            title=WindowConfig.TITLE
        )
        
    
    def start_run(self) -> None:
        self.scene_manager = SceneManager(window=self)
        self.show_view(self.scene_manager.menu_scene)
