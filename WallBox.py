from box import *
from pygame_utile import *

class WallBox(box):
    
    def __init__(self,screen,x,y):
        super().__init__(screen,x,y)
        self.rect = pygame.Rect(self.x,self.y,25,25)
        self.descripteur = 1
    
    def getDescriptif(self):
        return self.descripteur
    
    def draw(self):
        pygame.draw.rect(self.screen,(0,0,0),self.rect)
    