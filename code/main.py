import pygame
from sys import exit
from settings import *
from level import Level

class Game:
    def __init__(self):
        # pygame setup
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Zelda')
        pygame.display.set_icon(pygame.image.load('../graphics/icon/icon.jpg'))
        self.clock = pygame.time.Clock()

        # level setup
        self.level = Level()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


game = Game()
game.run()