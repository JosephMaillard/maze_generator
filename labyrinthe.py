from EmptyBox import EmptyBox
from WallBox import WallBox
from DepartureBox import DepartureBox
from ArrivalBox import ArrivalBox
from pygame_utile import *
import random as rd
import time
import pygame

class labyrinthe:

    def __init__(self,screen) -> None:
        
        self.Box_list = []
        self.wall_int = 0
        self.screen = screen
        for i in range(red_width):
            Box_width_list = []
            for j in range(red_height):
                if (j==0) or (j == red_height-1):
                    box = WallBox(screen,i*25,j*25)
                    self.wall_int +=1
                elif (i==0) or (i == red_width-1):
                    box = WallBox(screen,i*25,j*25)
                    self.wall_int +=1
                else:
                    box = EmptyBox(screen,i*25,j*25)
                Box_width_list.append(box)
            self.Box_list.append(Box_width_list)
        self.Box_list[1][1]= DepartureBox(screen,25,25)
        self.Box_list[red_width-2][red_height-2]= ArrivalBox(screen,(red_width-2)*25,(red_height-2)*25)

        self.arrival = self.Box_list[red_width-2][red_height-2]
        self.departure = self.Box_list[1][1]
    
    def getBox_list(self):
        return self.Box_list
    
    def draw(self):
        for i in range(red_width):
            for j in range(red_height):
                self.Box_list[i][j].draw()
    
    def getWall_int(self):
        return self.wall_int
    
    def set_Wall(self,a,b):
        self.Box_list[a][b] = WallBox(self.screen,a*25,b*25)
    
    def get_arrival(self):
        return self.arrival
    def get_departure(self):
        return self.departure
    
    """def update1(self):
        cond = True
        while cond:
            self.Box_list[5][1] = WallBox(self.screen,5*25,1*25)
            self.Box_list[4][2] = WallBox(self.screen,4*25,2*25)
            self.Box_list[5][3] = WallBox(self.screen,5*25,3*25)
            self.wall_int += 3
            self.draw()
            a = 6
            b = 2
            box = self.Box_list[a][b]
            if box.getDescriptif()== 0:

                self.Box_list[a][b] = WallBox(self.screen,a*25,b*25)
                self.wall_int += 1
                cond = False
                if (self.Box_list[a-1][b].getDescriptif() !=1):
                    if (self.Box_list[a+1][b].getDescriptif() !=1):
                        if (dijkstra(self,a-1,b,a+1,b) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            print("1")
                            break
                        else:
                            pass
                    if (self.Box_list[a][b-1].getDescriptif() !=1):
                        if (dijkstra(self,a-1,b,a,b-1) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                    if (self.Box_list[a][b+1].getDescriptif() !=1):
                        if (dijkstra(self,a-1,b,a,b+1) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                if (self.Box_list[a][b-1].getDescriptif() !=1):
                    if (self.Box_list[a][b+1].getDescriptif() !=1):
                        if (dijkstra(self,a,b-1,a,b+1) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                    if (self.Box_list[a+1][b].getDescriptif() !=1):
                        if (dijkstra(self,a,b-1,a+1,b) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                if (self.Box_list[a+1][b].getDescriptif() !=1):
                    if (self.Box_list[a][b+1].getDescriptif() !=1):
                        if (dijkstra(self,a+1,b,a,b+1) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                else:
                    pass"""


    
    def update(self):
        cond = True
        while cond:
            a = rd.randrange(1,red_width-1)
            b = rd.randrange(1,red_height-1)
            box = self.Box_list[a][b]
            if box.getDescriptif()== 0:

                self.Box_list[a][b] = WallBox(self.screen,a*25,b*25)
                pygame.draw.rect(self.screen,(0,0,255),pygame.Rect(a*25,b*25,25,25))
                self.wall_int += 1
                cond = False
                if (self.Box_list[a-1][b].getDescriptif() !=1):
                    if (self.Box_list[a+1][b].getDescriptif() !=1):
                        if (dijkstra(self,a-1,b,a+1,b) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                    if (self.Box_list[a][b-1].getDescriptif() !=1):
                        if (dijkstra(self,a-1,b,a,b-1) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                    if (self.Box_list[a][b+1].getDescriptif() !=1):
                        if (dijkstra(self,a-1,b,a,b+1) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                if (self.Box_list[a][b-1].getDescriptif() !=1):
                    if (self.Box_list[a][b+1].getDescriptif() !=1):
                        if (dijkstra(self,a,b-1,a,b+1) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                    if (self.Box_list[a+1][b].getDescriptif() !=1):
                        if (dijkstra(self,a,b-1,a+1,b) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                if (self.Box_list[a+1][b].getDescriptif() !=1):
                    if (self.Box_list[a][b+1].getDescriptif() !=1):
                        if (dijkstra(self,a+1,b,a,b+1) == False):
                            self.Box_list[a][b] = EmptyBox(self.screen,a*25,b*25)
                            self.wall_int -= 1
                            break
                        else:
                            pass
                else:
                    pass
                    




def dijkstra(lab,a,b,c,d):
    list1 = lab.getBox_list()
      #list3 sert à indiquer si les sommets ont déjà été visité
    list2 = [[red_height*red_width +20 for j in range(red_height)] for i in range(red_width)]
    list3 = [[False for j in range(red_height)] for i in range(red_width)]

    list2[a][b] = 0
    list3[a][b] = True
    p = a
    z = b
    while not ((a == c) and (b == d)):
        if (list1[a+1][b].getDescriptif() != 1):
            if (list2[a+1][b] > list2[a][b]+1):
                list2[a+1][b] = list2[a][b]+1
        if (list1[a-1][b].getDescriptif() != 1):
            if (list2[a-1][b] > list2[a][b]+1):
                list2[a-1][b] = list2[a][b]+1
        if (list1[a][b+1].getDescriptif() != 1):
            if (list2[a][b+1] > list2[a][b]+1):
                list2[a][b+1] = list2[a][b]+1
        if (list1[a][b-1].getDescriptif() != 1):
            if (list2[a][b-1] > list2[a][b]+1):
                list2[a][b-1] = list2[a][b]+1
        list3[a][b] = True
        (a,b) = min(list2,list3)
        if (list2[a][b] == red_height*red_width +20):
            #time.sleep(10)
            return False
    return True



def min(list2,list3):
    u,b = 0,0
    min = list2[u][b]
    for i in range(red_width):
        for j in range(red_height):
            if ((list2[i][j]<min) and (list3[i][j] == False)):
                min = list2[i][j]
                u,b = i,j
    return u,b