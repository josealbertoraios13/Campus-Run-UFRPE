"""
Configurações centralizadas
"""

class PlayerConfig:
    VELOCITY = 500
    JUMP_FORCE = 1000

    # Para as animações
    IDLE_FRAME_RATE = 0.07
    RUN_FRAME_RATE = 0.05

    START_X = 800
    START_Y = 200

    # Para assets
    IDLE_SPRITE = "assets/sprite/player/beto-idle.png"
    RUN_SPRITE = "assets/sprite/player/beto-run.png"
    SPRITE_SIZE = (256, 256)
    SPRITE_COLUMNS = 5
    IDLE_FRAME_COUNT = 25
    RUN_FRAME_COUNT = 25

class CameraConfig:
    ZOOM = 0.75
    LERP_FACTOR = 0.1
    OFFSET_Y = 160

class PhysicsConfig:
    GRAVITY = 1

    GROUND_WIDTH_MULTIPLIER = 5
    GROUND_HEIGHT = 140
    GROUND_COLOR = (101, 67, 33) # RGB

class RainConfig:
    DROP_COUNT = 1000
    MIN_SPEED = 500
    MAX_SPEED = 900
    MIN_WIDTH = 1
    MAX_WIDTH = 3
    COLOR = (76, 95, 115) # rgb

class VisualConfig:
    BACKGROUND_COLOR = (52, 73, 94) # rgb

    # fonts
    FONT_PATH = "assets/font/Jersey10-Regular.ttf"
    FONT_NAME = "Jersey 10"

    # menu
    MENU_IMAGE = "assets/images/main_menu.png"
    MENU_TITLE_SIZE = 82
    MENU_SUBTITLE_SIZE = 20

class GameConfig:
    WINDOW_WIDTH  = 1280
    WINDOW_HEIGHT = 720
    TITLE = "Campus Run: UFRPE"
    FPS = 60