import arcade
from game.player import Player
from game.scene_object import SceneObject
from game.camera import Camera
from game.rain_system import RainSystem

from utils import WINDOW_WIDTH

BACKGROUND_COLOR = (52, 73, 94)

class GameManager(arcade.View):

    def __init__(self) -> None:
        super().__init__()

        self.camera = Camera()

        self.background_color = BACKGROUND_COLOR

        self.rain = RainSystem()

        self.departament_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.plataform_list = arcade.SpriteList()

        self.ground = arcade.SpriteSolidColor(
            width=WINDOW_WIDTH * 5,
            height=140,
            color=arcade.color.DARK_BROWN
        )

        self.ground.center_x = WINDOW_WIDTH / 2
        self.ground.center_y = -50

        self.plataform_list.append(self.ground)  

        self.player = Player()

        self.ceagri2 = SceneObject(path="assets/images/ceagri2.png", x=3000, y=400)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            walls=self.plataform_list,
            gravity_constant=1
        )      
        
        self.player.start(player_list=self.player_list, physics_engine=self.physics_engine)

        self.ceagri2.start(scene_object_list=self.departament_list)

    def on_update(self, delta_time: float) -> bool | None:
        self.player.update()
        self.plataform_list.update()
        self.physics_engine.update()

        self.camera.behaviuor_update(player=self.player)

        self.rain.behaviour_update(delta_time=delta_time, camera=self.camera)

        self.player.behaviuor_update(delta_time=delta_time)
        self.player.update_animation(delta_time=delta_time)

    def on_draw(self) -> bool | None:
        self.clear()
        self.camera.use()
        
        self.departament_list.draw()        
        self.rain.rain_shapes.draw()
        self.plataform_list.draw()
        self.player_list.draw()   


    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        self.player.key_event(symbol=symbol)

    def on_key_release(self, symbol: int, modifiers: int) -> bool | None:
        self.player.key_event(symbol=symbol)
