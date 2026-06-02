from utils import WINDOW_WIDTH, WINDOW_HEIGHT, TITLE
from game import Game
import arcade

def main():
    window =  arcade.Window(width=WINDOW_WIDTH, height= WINDOW_HEIGHT, title=TITLE)

    game =  Game()

    window.show_view(game)

    arcade.run()

if __name__ == "__main__":
    main()