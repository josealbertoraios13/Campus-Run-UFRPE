"""
Estados, eventos e tipos
"""

from enum import Enum

class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"

class PlayerState(Enum):
    IDLE = "idle"
    RUNNING = "running"
    JUMPING = "jumping"
    FALLING = "falling"

class Direction():
    LEFT = -1
    RIGHT = 1

class EventType(Enum):
    # player
    PLAYER_MOVED = "player_moved"
    PLAYER_JUMPED = "player_jumped"
    PLAYER_LANDED = "player_landed"

    # game
    GAME_STARTED = "game_started"
    GAME_PAUSED = "game_paused"
    GAME_RESUMED = "game_resumed"
    GAME_OVER = "game_over"

    # camera
    CAMERA_MOVED = "camera_moved"