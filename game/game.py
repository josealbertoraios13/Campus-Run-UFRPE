import arcade

class Game(arcade.View):
    """
        Main application class.

        NOTE: Go ahead and delete the methods you don't need.
        If you do need a method, delete the 'pass' and replace it
        with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self) -> None:
        super().__init__()

        self.background_color = arcade.color.AMAZON

        # If you have sprite lists, you should create them here,
        # and set them to None
    
    def reset(self):
        """Reset the game to the initial state."""
        pass

    def on_draw(self) -> bool | None:
        """Render the screen"""
        return super().on_draw()
    
    def on_update(self, delta_time: float) -> bool | None:
        """
            All the logic to move, and the game logic goes here.
            Normally, you will call update() on the sprites lists that
            need it.
        """
        return super().on_update(delta_time)
    
