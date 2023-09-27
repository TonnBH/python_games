import  pygame
from settings import *
from tiles import Tile
from player import  Player

class Level:
    def __init__(self):

        self.display_suraface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP_01):
           for col_index, col in enumerate(row):
               x = col_index * TILESIZE
               y = row_index * TILESIZE
               if col == 'X':
                   Tile((x,y),[self.visible_sprites,self.obstacle_sprites])

               if col == 'P':
                   self.player = Player((x,y),[self.visible_sprites])


    def run(self):
        self.visible_sprites.draw(self.display_suraface)
        self.visible_sprites.update()