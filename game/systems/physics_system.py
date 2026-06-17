from game.core import System, PlayerConfig
from game.entities import Player

class PhysicsSystem(System):

    def __init__(self,player: Player) -> None:
        self.player = player

    def update(self, delta_time: float) -> None:
        self._update_horizontal_movement(delta_time=delta_time)

        self._update_vertical_moviment(delta_time=delta_time)

        self._update_direction()

    def _update_horizontal_movement(self, delta_time: float) -> None:
        if self.player.left_pressed and self.player.right_pressed:
            self.player.change_x = 0
            self.player.is_running = False
            return
        
        if self.player.left_pressed:
            self.player.change_x = -PlayerConfig.VELOCITY * delta_time
            self.player.is_running = True
        
        elif self.player.right_pressed:
            self.player.change_x = PlayerConfig.VELOCITY * delta_time
            self.player.is_running = True

        else:
            self.player.is_running = False
            self.player.change_x = 0

    def _update_vertical_moviment(self, delta_time: float) -> None:
        if self.player.jumped and self.player.physics_engine.can_jump():
            self.player.change_y = PlayerConfig.JUMP_FORCE * delta_time

    def _update_direction(self) -> None:
        if self.player.right_pressed and not self.player.left_pressed:
            self.player.facing_right = False
            self.player.scale_x = 1
            
        elif self.player.left_pressed and not self.player.right_pressed:
            self.player.facing_right = True
            self.player.scale_x = -1  