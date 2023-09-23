from box import *
from pygame_utile import *

class ArrivalBox(box):
    
    def __init__(self,screen,x,y):
        super().__init__(screen,x,y)
        self.descripteur = 3
    
    def getDescriptif(self):
        return self.descripteur
    
    def draw(self):
        pygame.draw.rect(self.screen,(255,0,0),self.rect)