from box import *
from pygame_utile import *

class DepartureBox(box):
    
    def __init__(self,screen,x,y):
        super().__init__(screen,x,y)
        self.descripteur = 2
    
    def getDescriptif(self):
        return self.descripteur
    
    def draw(self):
        pygame.draw.rect(self.screen,(0,255,0),self.rect)