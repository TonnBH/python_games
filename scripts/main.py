import pygame, sys
import pygame.display
from settings import
from level_01 import Level
from debug import debug
pygame.display.init()
info = pygame.display.Info()
print(info)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.clock = pygame.time.Clock()

        self.level_01 = Level()
        #self.level_01.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            self.screen.fill('black')
            self.level_01.run()
            pygame.display.update()
            self.clock.tick(FPS)
            #self.clock.get_rawtime()

if __name__ == '__main__':
    game = Game()
    game.run()
