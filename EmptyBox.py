from box import *
from pygame_utile import *

class EmptyBox(box):
    
    def __init__(self,screen,x,y):
        super().__init__(screen,x,y)
        self.screen = screen
        self.descripteur = 0
        self.isInPath = False
        self.rect = pygame.Rect(self.x,self.y,25,25)
    
    def draw(self):
        if self.isInPath == False:
            pygame.draw.rect(self.screen,(255,255,255),self.rect)
        else:
            pygame.draw.rect(self.screen,(255,255,0),self.rect)

    def getDescriptif(self):
        return self.descripteur
    
    def get_X(self):
        return self.x
    
    def set_isInPath(self):
        self.isInPath = True
    
    def get_isInPath(self):
        return self.isInPath
    
