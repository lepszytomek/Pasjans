import pygame, sys, math


class Game(object):


    def __init__(self):
        pygame.init()
        self.screen_x = 1500
        self.screen_y = 1000
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))



        while True:
            # manewrowanie oknem
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)









if __name__ == "__main__":
    Game()

