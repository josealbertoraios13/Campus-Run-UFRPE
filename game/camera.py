import arcade

class Camera(arcade.Camera2D):

    def __init__(self) -> None:
          super().__init__()

    def start(self) -> None:
         self.zoom = 0.75

    def behaviuor_update(self, player: arcade.Sprite) -> None:
        current_position = arcade.Vec2(
            self.position[0],
            self.position[1]
        )

        target_position = arcade.Vec2(
            player.position[0],
            player.position[1] + 160
        )
        
        self.position = arcade.math.lerp_2d(
            current_position, 
            target_position,
            0.1
        )