from game.entities import SceneObject
from game.core.config import VehiclesConfig

import arcade

class VehiclesSceneManager:

    def __init__(self) -> None:
        self.vehicles = {}
        for vehicle_name, config in VehiclesConfig.VEHICLES.items():
            vehicle = SceneObject(
                path=config["path"],
                x=config["x"],
                y=config["y"]
            )
            vehicle.scale = config["scale"]
            self.vehicles[vehicle_name] = vehicle
        
        # Manter compatibilidade com acessos diretos
        self.uno = self.vehicles["uno"]
        self.gol = self.vehicles["gol"]
        self.hb20 = self.vehicles["hb20"]
        self.byd = self.vehicles["byd"]
        self.scania = self.vehicles["scania"]
        self.bus = self.vehicles["bus"]

    def on_spawn(self, sprite_list: arcade.SpriteList) -> None:
        for vehicle in self.vehicles.values():
            sprite_list.append(vehicle)