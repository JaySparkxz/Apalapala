import pygame 
from tiles import Tile
from setting import tile_size
class Level:
    def __init__(self, level_data, surface):

        # LEVEL SETUP
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0 

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'X':
                    x, y = col_index*tile_size, row_index*tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(2)
        self.tiles.draw(self.display_surface)
        