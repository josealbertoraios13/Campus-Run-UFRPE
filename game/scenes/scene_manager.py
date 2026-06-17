from game.scenes.game_scene import GameScene
from game.scenes.menu_scene import MenuScene
from game.scenes.win_scene import WinScene

import arcade

class SceneManager:
    def __init__(self, window: arcade.Window) -> None:
        self.window = window
        self.win_scene = None
        self.menu_scene = MenuScene()
        self.menu_scene.window = window
        self.current_scene = "menu"
    
    def switch_to_game(self) -> None:
        self.game_scene = GameScene()
        self.game_scene.window = self.window
        
        self.window.show_view(self.game_scene)
        self.current_scene = "game"
    
    def switch_to_win(self, status) -> None:
        self.win_scene = WinScene(status=status)  # recria sempre com status atualizado
        self.win_scene.window = self.window
        self.window.show_view(self.win_scene)
        self.current_scene = "win"

    def switch_to_menu(self) -> None:
        self.window.show_view(self.menu_scene)
        self.current_scene = "menu"
