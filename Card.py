import pygame


class Card(object):


    def __init__(self, Game, size, position, type):
        #type (value *1-13*, color *1-4*), ex. (3, 2)
        #colors 1:spades(pik) 2:hearts(kier) 3:diamonds(karo) 4:clubs(trefl)
        self.Game = Game
        self.size = size
        self.position = position
        self.type = type
        self.rect = pygame.Rect(self.position, self.size)   #Potencjalnie można tu dodać zaokrąglanie rogów
        self.open = False

    def draw(self):

        pygame.draw.rect(self.game.screen, (200, 50, 50), self.rect)