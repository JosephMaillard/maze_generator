import pygame
from pygame_utile import *
from labyrinthe import *
import time
from DFS import DFS
from dijkstra import dijkstra2

def main():

    screen = pygame.display.set_mode((width, height))
    pygame.init()
    continuer = True
    test = labyrinthe(screen)

    arrival = test.get_arrival()
    departure = test.get_departure()

    test.draw()
    dij = False
    while continuer:
    # Gérer les événements
        test.draw()
        if (test.getWall_int() < 1020):
            test.update()
            #if test.getWall_int() == 1020:
                #print("hola")
                #dijkstra2(test,departure.get_X(),departure.get_Y(),arrival.get_X(),arrival.get_Y())
            


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
        
        


        # Rafraîchir l'écran
        pygame.display.update()

# Quitter Pygame
pygame.quit()




if __name__ == "__main__":

    main()