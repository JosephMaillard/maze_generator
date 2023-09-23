#from labyrinthe import labyrinthe
from EmptyBox import EmptyBox
from WallBox import WallBox
from pygame_utile import *
from antecedent import antecedent

def get_sucessors(lab,list,a,b):

    pass

def min(list,list3):
    u,b = 0,0
    min = list[u][b]
    for i in range(red_width):
        for j in range(red_height):
            if ((list[i][j]<min) and (list3[i][j] == False)):
                min = list[i][j]
                u,b = i,j
    return u,b



def dijkstra2(lab,a,b,c,d):
    list1 = lab.getBox_list()
      #list3 sert à indiquer si les sommets ont déjà été visité
    list2 = [[red_height*red_width +20 for j in range(red_height)] for i in range(red_width)]
    list3 = [[False for j in range(red_height)] for i in range(red_width)]

    list2[a][b] = 0
    list3[a][b] = True

    ant =antecedent()

    p = a
    z = b
    while not ((a == c) and (b == d)):
        if (list1[a+1][b].getDescriptif() != 1):
            if (list2[a+1][b] > list2[a][b]+1):
                list2[a+1][b] = list2[a][b]+1
                ant.add(list1[a+1][b],list1[a][b])

        if (list1[a-1][b].getDescriptif() != 1):
            if (list2[a-1][b] > list2[a][b]+1):
                list2[a-1][b] = list2[a][b]+1
                ant.add(list1[a-1][b],list1[a][b])

        if (list1[a][b+1].getDescriptif() != 1):
            if (list2[a][b+1] > list2[a][b]+1):
                list2[a][b+1] = list2[a][b]+1
                ant.add(list1[a][b+1],list1[a][b])

        if (list1[a][b-1].getDescriptif() != 1):
            if (list2[a][b-1] > list2[a][b]+1):
                list2[a][b-1] = list2[a][b]+1
                ant.add(list1[a][b-1],list1[a][b])

        list3[a][b] = True
        (a,b) = min(list2,list3)
        
        #pygame.draw.rect(lab.screen,(0,0,255),pygame.Rect(p*25,z*25,25,25))
    
    while not ((a == p) and (b == z)):
        previous_box = ant.get_key(list1[a][b])
        previous_box.set_isInPath()
        a = previous_box.get_X()
        b = previous_box.get_Y()
        print(a,b)
