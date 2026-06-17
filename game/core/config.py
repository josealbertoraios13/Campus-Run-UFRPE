class PlayerConfig:
    VELOCITY = 500
    JUMP_FORCE = 1000

    # Para as animações
    IDLE_FRAME_RATE = 0.07
    RUN_FRAME_RATE = 0.05

    START_X = 3000
    START_Y = 200

    # Para assets
    IDLE_SPRITE = "assets/sprites/player/beto-idle.png"
    RUN_SPRITE = "assets/sprites/player/beto-run.png"
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
    GROUND_COLOR = (101, 67, 33, 255)  # RGBA (marrom escuro opaco)

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
    WIN_IMAGE = "assets/images/win_menu.png"
    MENU_TITLE_SIZE = 82
    MENU_SUBTITLE_SIZE = 20

class VehiclesConfig:
    VEHICLES = {
        "uno": {
            "path": "assets/images/uno.png",
            "x": -1000,
            "y": 110,
            "scale": 0.35
        },
        "gol": {
            "path": "assets/images/gol.png",
            "x": -6000,
            "y": 120,
            "scale": 0.35
        },
        "hb20": {
            "path": "assets/images/hb20.png",
            "x": 2000,
            "y": 100,
            "scale": 0.35
        },
        "byd": {
            "path": "assets/images/byd.png",
            "x": -4000,
            "y": 115,
            "scale": 0.35
        },
        "scania": {
            "path": "assets/images/scania.png",
            "x": -11000,
            "y": 265,
            "scale": 0.70
        },
        "bus": {
            "path": "assets/images/bus.png",
            "x": 4500,
            "y": 200,
            "scale": 0.76
        }
    }

class GameConfig:
    WINDOW_WIDTH  = 1280
    WINDOW_HEIGHT = 720
    TITLE = "Campus Run: UFRPE"
    FPS = 60