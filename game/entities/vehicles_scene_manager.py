from game.entities import SceneObject
from game.core.config import VehiclesConfig

import arcade

class VehiclesSceneManager:
    def __init__(self) -> None:
        self.vehicles: dict[str, SceneObject] = {}
        self._spawned = False

        for vehicle_name, config in VehiclesConfig.VEHICLES.items():
            vehicle = SceneObject(
                path=config["path"],
                x=config["x"],
                y=config["y"]
            )
            vehicle.scale = config["scale"]
            self.vehicles[vehicle_name] = vehicle
        
    def __getattr__(self, name: str) -> SceneObject:
        vehicles = self.__dict__.get("vehicles", {})
        if name in vehicles:
            return vehicles[name]
        
        raise AttributeError(f"Veículo '{name}' não encontrado.")

    def on_spawn(self, sprite_list: arcade.SpriteList) -> None:
        if self._spawned:
            return

        for vehicle in self.vehicles.values():
            sprite_list.append(vehicle)

        self._spawned = True