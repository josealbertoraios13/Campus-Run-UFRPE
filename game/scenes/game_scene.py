from game.entities import Player, SceneObject, VehiclesSceneManager, TowelsSceneManager, WinTrigger
from game.systems import InputSystem, PhysicsSystem, AnimationSystem, CameraSystem, RainSystem, HudSystem
from game.core import PhysicsConfig, VisualConfig, WindowConfig

import arcade

class GameScene(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        
        self.background_color = VisualConfig.BACKGROUND_COLOR
        
        self.departament_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.obstacle = arcade.SpriteList()
        self.plataform_list = arcade.SpriteList()
        self.trigger_win_list = arcade.SpriteList()
        self.towels = arcade.SpriteList()
        
        self._setup_platforms()

        self.hud = HudSystem()
        
        self.player = Player()
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            walls=[self.plataform_list, self.obstacle],
            gravity_constant=PhysicsConfig.GRAVITY
        )
        self.player.physics_engine = self.physics_engine
        
        self.player.on_spawn(
            sprite_list=self.player_list,
            physics_engine=self.physics_engine
        )

        self.win_trigger = WinTrigger(window=self.window)
        
        self.win_trigger.on_spawn(
            sprite_list=self.trigger_win_list,
            physics_engine=self.physics_engine
        )
        
        self.input_system = InputSystem(self.player)
        self.physics_system = PhysicsSystem(self.player)
        self.animation_system = AnimationSystem(self.player)

        self.camera = arcade.Camera2D()
        self.camera_system = CameraSystem(camera=self.camera, player=self.player)
        
        self.gui_camera = arcade.Camera2D()
        self.ceagri2 = SceneObject(
            path="assets/images/ceagri2.png",
            x=3000,
            y=390
        )

        self.ceagri2.on_spawn(
            sprite_list=self.departament_list,
            physics_engine=self.physics_engine
        )

        self.bar_da_curva = SceneObject(
            path="assets/images/bar-da-curva.png",
            x=0,
            y=200
        )

        self.bar_da_curva.scale = 0.75

        self.bar_da_curva.on_spawn(
            sprite_list=self.departament_list,
            physics_engine=self.physics_engine
        )

        self.ufrpe = SceneObject(
            path="assets/images/ufrpe.png",
            x=-5000,
            y=450
        )

        self.ufrpe.scale = 2

        self.ufrpe.on_spawn(
            sprite_list=self.departament_list,
            physics_engine=self.physics_engine
        )

        self.deinfo = SceneObject(
            path="assets/images/deinfo.png",
            x=-10000,
            y=300
        )

        self.deinfo.on_spawn(
            sprite_list=self.departament_list,
            physics_engine=self.physics_engine
        )
        
        self.obstacle_manager = VehiclesSceneManager()
        self.obstacle_manager.on_spawn(self.obstacle)

        self.towels_manager = TowelsSceneManager(window=self.window)
        self.towels_manager.on_spawn(sprite_list=self.towels, physics_engine=self.physics_engine)

        self.rain = RainSystem()
    
    def _setup_platforms(self) -> None:
        ground_texture = arcade.load_texture("assets/images/ground.png")
        
        platform_scale = 0.4
        tile_width = ground_texture.width * platform_scale 
        
        total_width = WindowConfig.WINDOW_WIDTH * PhysicsConfig.GROUND_WIDTH_MULTIPLIER
        num_tiles = int(total_width / tile_width) + 50
        
        start_x = -13000
        
        self.ground_tiles = []
        for i in range(num_tiles):
            tile = arcade.Sprite(
                "assets/images/ground.png",
                scale=platform_scale
            )

            tile.center_x = start_x + (i * (tile_width - 40))
            tile.center_y = -225
            
            self.plataform_list.append(tile)
            self.ground_tiles.append(tile)
    
    def on_update(self, delta_time: float) -> None:
        self.player.update()
        
        self.plataform_list.update()
        
        self.physics_engine.update()

        self.obstacle.update()
        self.towels.update()
        
        self.physics_system.update(delta_time) 
        self.animation_system.update(delta_time)   
        self.camera_system.update(delta_time)          
        
        self.rain.behaviour_update(delta_time, self.camera)
        
        self.hud.update(delta_time=delta_time)

        if self.hud.wetness_level >= 100:
            self.window.scene_manager.switch_to_lose() # type: ignore

        self.win_trigger.check_trigger(sprite_list=self.player_list) 
        self.towels_manager.check_triggers(sprite_list=self.player_list)
    
    def on_draw(self) -> None:
        self.clear()
        
        self.camera.use()
        
        self.departament_list.draw()
        self.obstacle.draw()
        self.towels.draw()
        self.rain.rain_shapes.draw() 
        self.plataform_list.draw()
        self.player_list.draw()

        self.trigger_win_list.draw()

        self.gui_camera.use()
        self.hud.draw()
    
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.input_system.on_key_press(symbol)

        if symbol == arcade.key.ESCAPE:
            self.window.scene_manager.switch_to_menu() # type: ignore
    
    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.input_system.on_key_release(symbol)