import os
from ursina import load_texture

CHUNKSIZE = 5
WORLDSIZE = 10

DETAIL_DISTANCE = 20
DEFAULT_TEXTURE = 0
BASE_DIR = os.getcwd()
IMG_DIR = os.path.join(BASE_DIR, 'assets/blocks')

block_textures = []

file_list = os.listdir(IMG_DIR)
for image in file_list:
    texture  = load_texture('assets/blocks' + os.sep + image)
    block_textures.append(texture)
