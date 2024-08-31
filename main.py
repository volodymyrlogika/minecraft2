from ursina import *
from ursina import Default, camera
from ursina.prefabs.first_person_controller import FirstPersonController

from numpy import floor
from perlin_noise import PerlinNoise

app = Ursina()
MAPSIZE = 20

class Block(Button):
    def __init__(self, pos, **kwargs):
        super().__init__(
            parent=scene, #батьківський елемент
            model='cube', # модель
            texture='assets\\block_textures\\grass.png',
            scale=1,
            collider='box',
            position=pos,
            color=color.color(0,0, random.uniform(0.9, 1)),
            origin_y=-0.5,
            **kwargs)



player  = FirstPersonController()

sky = Sky(texture='sky_sunset')

# axe = Entity(model='assets\\minecraft_diamond-pickaxe\\scene', scale=0.05, collider='box')

# ground = Entity(model="quad", texture="grass", scale=64, textute_scale=(16,16) ,rotation=90, 
#                 collider='box', position=(-2, 0,0))


noise = PerlinNoise(octaves=3, seed=4522)


for x in range(-MAPSIZE, MAPSIZE):
    for z in range(-MAPSIZE,MAPSIZE):
        y = floor(noise([x/24, z/24])*6)
        block = Block((x,y,z))
      

window.fullscreen = True
app.run()
