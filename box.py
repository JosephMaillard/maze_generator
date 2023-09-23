from pygame_utile import *
import pygame

class box():

    def __init__(self,screen,x,y):
        self.x = x
        self.y = y
        self.screen = screen
        self.rect = pygame.Rect(self.x,self.y,25,25)
        self.descripteur = 0
    
    def draw(self):
        pygame.draw.rect(self.screen,(0,0,255),self.rect)
    
    def getDescriptif(self):
        return self.descripteur
    
    def get_X(self):
        return self.x//red_width
    
    def get_Y(self):
        return self.y//red_height
    
    def set_isInPath(self):
        pass