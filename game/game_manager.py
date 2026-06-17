from game.scenes.scene_manager import SceneManager
from game.core import GameConfig
import arcade

class GameManager(arcade.Window):
    def __init__(self) -> None:
        super().__init__(
            width=GameConfig.WINDOW_WIDTH,
            height=GameConfig.WINDOW_HEIGHT,
            title=GameConfig.TITLE
        )
        
        self.scene_manager = SceneManager(window=self)
        self.show_view(self.scene_manager.menu_scene)
