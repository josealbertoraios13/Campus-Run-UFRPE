import arcade

class SceneObject(arcade.Sprite):
    def __init__(self, path: str, x: float, y: float) -> None:
        super().__init__()

        self.texture  = arcade.load_texture(path)

        self.center_x = x
        self.center_y = y

    def start(self, scene_object_list: arcade.SpriteList) -> None:
        scene_object_list.append(self)
        
