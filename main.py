from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor

app = Ursina()
from settings import *
from models import Block, WorldEdit

player  = FirstPersonController()
player.x = CHUNKSIZE/2
player.z = CHUNKSIZE/2
player.y = 20
player.gravity = 0.5

sky = Sky()
light = DirectionalLight(shadows=True)
light.look_at(Vec3(1,-1,1))

world = WorldEdit()
world.generate_world()
# scene.fog_density = (5, 50)   # sets linear density start and end
# axe = Entity(model='assets\\minecraft_diamond-pickaxe\\scene', scale=0.05, collider='box')

camera.clip_plane_far = 30
window.fullscreen = True
app.run()
