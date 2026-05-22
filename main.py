from game import Game
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

TITLE = "Campus Run: UFRPE"

def main():
    window =  arcade.Window(width=WINDOW_WIDTH, height= WINDOW_HEIGHT, title=TITLE)

    game =  Game()

    window.show_view(game)

    arcade.run()

if __name__ == "__main__":
    main()