import pygame
from run import game


class Card(object):


    def __init__(self, size, position, type):
        #type (value *1-13*, color *0-3*), ex. (3, 2)
        #colors 0:spades(pik) 1:hearts(kier) 2:diamonds(karo) 3:clubs(trefl)
        self.game = game
        self.size = size
        self.position = position
        self.type = type
        self.rect = pygame.Rect(self.position, self.size)   #Potencjalnie można tu dodać zaokrąglanie rogów

    def draw(self):
        pygame.draw.rect(self.game.screen, (200, 50, 50), self.rect)