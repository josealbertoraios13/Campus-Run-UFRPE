from game import GameManager
import arcade

def main():
    game_manager = GameManager()
    game_manager.start_run()
    arcade.run()

if __name__ == "__main__":
    main()