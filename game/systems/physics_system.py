from entities import Player
player_velocity = 500
jump_force = 1000
class PhysicsSystem:
    def update(self, player: Player, delta_time: float) -> None:
        if player.left_pressed and not player.right_pressed:
            player.change_x = -player_velocity * delta_time
            player.is_running = True
            player.facing_right = True
        
        elif player.right_pressed and not player.left_pressed:
            player.change_x = player_velocity * delta_time
            player.is_running = True
            player.facing_right = False

        else:
            player.is_running = False
            player.change_x = 0

        if player.jumped and player.physics_engine.can_jump():
            player.change_y = jump_force * delta_time

        if player.facing_right:
            player.scale_x = -1
        else:
            player.scale_x = 1        