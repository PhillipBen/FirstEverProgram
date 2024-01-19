import pygame
import numpy as np
import math

"""NOTE: This was the first python program I ever created. This is why it is very buggy.
Controls:
- ESC: Quit the game.
- Key 1:Create a basic tile map.
- Key 2:Get the current coordinates of your mouse
- Key 3:Create a new unit, inputing variables through the shell.
- Key 4:Generate a preset map.
- Mouse: Click on a unit (Circle) to move them. You control both teams. Click on the enemy to attack.
"""

#Initialization
screen = pygame.display.set_mode([800,900])
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_1,
    K_2,
    K_3,
    K_4
)

clickableObjectsList = [1,0]


pygame.init()
screen.fill((255,255,255))


#Sprites

class Player(pygame.sprite.Sprite):
    def __init__(self,px, py):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))#How big it is
        self.surf.fill((0, 0, 0))
        x = px * 30 + 40
        y = 1
        if px%2 == 1:
            y = py * 30 - 15 + 50
        else:
            y = py * 30 + 50
        for i in range(1,MapTNOT + 1):
            if int(HT[i,1]) == px and int(HT[i,2]) == py:
                if HT[i,3] == "player":
                    if HT[i,6] == "1": 
                        pygame.draw.circle(screen, (255,0,0), (x,y), 10) #RGB 
                    elif HT[i,6] == "2": 
                        pygame.draw.circle(screen, (0,0,255), (x,y), 10)
        
        
    def update(self, px, py):
        
           
        x = px * 30 + 40
        y = 1
        if px%2 == 1:
            y = py * 30 + 35
        else:
            y = py * 30 + 50


        
                    
                    
                    
        for i in range(1,MapTNOT + 1):
            if int(HT[i,1]) == px and int(HT[i,2]) == py:
                if HT[i,3] == "player":
                    print(allies)
                    print(HT[i,6])
                    print(HT)
                    
                    if HT[i,6] == "1": 
                        pygame.draw.circle(screen, (255,0,0), (x,y), 10) #RGB 
                    elif HT[i,6] == "2": 
                        pygame.draw.circle(screen, (0,0,255), (x,y), 10)
                    
        
            
            


class Tile(pygame.sprite.Sprite):
    def __init__(self,cloneID):
        super(Tile, self).__init__()
        self.surf = pygame.Surface((75, 25))#How big it is
        self.surf.fill((0, 0, 0))
        x = cloneID[0] * 30 + 20
        y = 1
        if cloneID[0]%2 == 1:
            y = cloneID[1] * 30 - 15 
        else:
            y = cloneID[1] * 30
        verticies = [(x, y+50), (x+11, y+36), (x+28.5, y+36), (x+39.5, y+50), (x+28.5, y+64.5), (x+11, y+64.5)]
        pygame.draw.polygon(screen, (0,0,0), (verticies))
        
        
       
    def update(self,hx,hy,pMU,c1,c2,c3):
        global HT
        global sID
        global hasPlayer
        global mouseClick
        global px
        global py
        
        #print(sameTile)
        i = sID
        
        if sameTile == True and int(HT[i,1]) == px and int(HT[i,2]) == py:
            HT[i,3]="player"
            player.update(int(HT[i,1]), int(HT[i,2]))
            

        
        
        
        if mouseClick == 3 and int(HT[i,1]) == px and int(HT[i,2]) == py and sameTile == False:
                
                
                
                
                for j in range(1,MapTNOT + 1):
                        if int(HT[j,1]) == hx and int(HT[j,2]) == hy:
                            
                            HT[i,3]="player"
                            HT[i,4]=HT[j,4]
                            HT[i,5]=HT[j,5]
                            HT[i,6]=HT[j,6]
                            HT[i,7]=HT[j,7]

                            
                                                                                                
                            HT[j,4]=0
                            HT[j,5]=0
                            HT[j,6]=0
                            HT[j,7]=0
        
        
        
        if pMU == False:
            
        
            x = int(hx) * 30 + 20
            y = 1
            if int(hx)%2 == 1:
                y = int(hy) * 30 - 15 
            else:
                y = int(hy) * 30
            verticies = [(x, y+50), (x+11, y+36), (x+28.5, y+36), (x+39.5, y+50), (x+28.5, y+64.5), (x+11, y+64.5)]

            

            pygame.draw.polygon(screen, (0,0,0), (verticies))
            
            
        elif pMU == True and int(HT[i,1]) != hx or int(HT[i,2]) != hy:
            
            sID += 1
            
            
        elif int(HT[i,1]) == hx and int(HT[i,2]) == hy:  #and HT[i,3] == "player"
            
            
            if HT[i,3] == "player" and mouseClick == 1:
                hasPlayer = True
            
                
            
            sID += 1
            
            
            x = int(hx) * 30 + 20
            y = 1
            if int(hx)%2 == 1:
                y = int(hy) * 30 - 15 
            else:
                y = int(hy) * 30
            verticies = [(x, y+50), (x+11, y+36), (x+28.5, y+36), (x+39.5, y+50), (x+28.5, y+64.5), (x+11, y+64.5)]
            pygame.draw.polygon(screen, (c1,c2,c3), (verticies))
            
            
            
            if mouseClick == 1:
                
                player.update(int(HT[i,1]), int(HT[i,2]))
                HT[i,3]="none"
        elif int(HT[i,1]) - hx <= 2 and int(HT[i,2]) - hy <= 2:
            print("Hai!!")
            #if (int(HT[j,1]) - int(HT[i,1])) <= 2 and (int(HT[j,2]) - int(HT[i,2])) <= 2: 
                #in range
                #inRange = True
                #print("in range")
            #else:
                #not in range
                #inRange = False
                #print("not in range")
                   
        
                
sprite_list = pygame.sprite.Group()
spritePList = pygame.sprite.Group()



cloneIDN = 0
def StartMap(): #Use L=25, H=26 for basic map
    #L = 3 #int(input("Length"))
    #H = 3 #int(input("Height"))
    CCL = 0
    CCH = 0
    
    for i in range(0, MapLength * MapHeight):
        
        global cloneIDN
        cloneID = (CCL, CCH)
        tile = Tile(cloneID)
        sprite_list.add(tile)
        cloneIDN += 1
        
        global HT

        
        HT = np.append(HT, [[cloneIDN, cloneID[0], cloneID[1],"none",0,0,0,0]], axis = 0)
        
        
        
        
        if CCL == MapLength - 1:
            CCH += 1
            CCL = 0
        else:
            CCL += 1
    



HT = np.array([[0,0,0,0,0,0,0,0]]) #HexagonTiles
#HT ItemName per Comma : Tile #, Tile X, Tile Y, Has player?(Player, none), DMG, HP, Team #, Alliance #

MapLength = 5
MapHeight = 5
MapTNOT = MapLength * MapHeight #MapTotalNumberOfTiles
sameTile = False


hx = 0
hy = 0

px = 0
py = 0
mouseClick = 0
sID = 1

px = 0
py = 0

px2 = 0
py2 = 0

TeamTurnNumber = 1
#Team 1 is red, Team 2 is blue

Team1 = [1]
Team2 = [2]
Team3 = []
Team4 = []
#add here to add to the max number of teams, and the first two numbers inside 1 & 2 are initializing enemies
TeamNumberTotal = 4
#This is the total amount of teams
#then go to key 3 press, and add a k if-statement in assigning teams

allies = False
inRange = False
playerDead = False

playerOn = False


hasPlayer = False


running  =  True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == KEYDOWN:
            if event.key == K_1:
                StartMap()
                print(HT)
                print(spritePList)
        if event.type == KEYDOWN:
            if event.key == K_2:
                
                m = pygame.mouse.get_pos(0)
                mx = m[0]
                my = m[1]
                
                
                print(mx)
                print(my)
                
                
                nx = math.floor((mx - 20)/ 30)
                
                print(nx)
                
                if nx%2 == 1:
                    ny = math.floor((my - 15)/ 30)
                else:
                    ny = math.floor((my-30)/ 30)
                
                print(ny)

        if event.type == KEYDOWN: #This is a map preset for a 1 v 1 Fight
            if event.key == K_4:
                MapLength = 10
                MapHeight = 10
                MapTNOT = MapLength * MapHeight
                StartMap()

                #Team1
                x=1
                HT[x,3]="player"
                HT[x,4]="5" #DMG
                HT[x,5]="30" #HP
                HT[x,6]="1" #Team #
                HT[x,7]="1" #Alliance #
                player = Player(px,py)
                player.update(0,0)

                x=2
                HT[x,3]="player"
                HT[x,4]="4" #DMG
                HT[x,5]="25" #HP
                HT[x,6]="1" #Team #
                HT[x,7]="1" #Alliance #
                player = Player(px,py)
                player.update(1,0)

                x=1 + MapLength
                HT[x,3]="player"
                HT[x,4]="3" #DMG
                HT[x,5]="20" #HP
                HT[x,6]="1" #Team #
                HT[x,7]="1" #Alliance #
                player = Player(px,py)
                player.update(0,1)

                x=3
                HT[x,3]="player"
                HT[x,4]="2" #DMG
                HT[x,5]="15" #HP
                HT[x,6]="1" #Team #
                HT[x,7]="1" #Alliance #
                player = Player(px,py)
                player.update(2,0)

                x=1 + (MapLength * 2)
                HT[x,3]="player"
                HT[x,4]="1" #DMG
                HT[x,5]="10" #HP
                HT[x,6]="1" #Team #
                HT[x,7]="1" #Alliance #
                player = Player(px,py)
                player.update(0,2)


                #Team 2
                x=MapLength * 10
                HT[x,3]="player"
                HT[x,4]="5" #DMG
                HT[x,5]="30" #HP
                HT[x,6]="2" #Team #
                HT[x,7]="2" #Alliance #
                player = Player(px,py)
                player.update(9,9)

                x=9 + (MapLength * 9)
                HT[x,3]="player"
                HT[x,4]="4" #DMG
                HT[x,5]="25" #HP
                HT[x,6]="2" #Team #
                HT[x,7]="2" #Alliance #
                player = Player(px,py)
                player.update(8,9)

                x=MapLength * 9
                HT[x,3]="player"
                HT[x,4]="3" #DMG
                HT[x,5]="20" #HP
                HT[x,6]="2" #Team #
                HT[x,7]="2" #Alliance #
                player = Player(px,py)
                player.update(9,8)

                x=8 + (MapLength * 9)
                HT[x,3]="player"
                HT[x,4]="2" #DMG
                HT[x,5]="15" #HP
                HT[x,6]="2" #Team #
                HT[x,7]="2" #Alliance #
                player = Player(px,py)
                player.update(7,9)

                x=MapLength * 8
                HT[x,3]="player"
                HT[x,4]="1" #DMG
                HT[x,5]="10" #HP
                HT[x,6]="2" #Team #
                HT[x,7]="2" #Alliance #
                player = Player(px,py)
                player.update(9,7)
                
                print(HT)
        if event.type == KEYDOWN:
            if event.key == K_3:
                screen.fill((255,255,255))
                player = Player(px,py)
                spritePList.add(player)
                px = int(input("X"))
                py = int(input("Y"))
                lvl = int(input("Unit LvL"))
                

                if lvl == 1:
                    DMG = 1
                    HP = 10
                elif lvl == 2:
                    DMG = 2
                    HP = 15
                elif lvl == 3:
                    DMG = 3
                    HP = 20
                elif lvl == 4:
                    DMG = 4
                    HP = 25
                elif lvl == 5:
                    DMG = 5
                    HP = 30
                
                Team = str(input("Team #"))

                
                playerMovementUpdate=False
                player.update(px, py)
                for i in range(1, MapTNOT + 1):
                    sprite_list.update(HT[i,1],HT[i,2],playerMovementUpdate,255,255,255)  #redraw the hexagon
                    
                    if HT[i,3] == "player": #tile already contains player
                        player.update(int(HT[i,1]),int(HT[i,2]))
                    
                    if int(HT[i,1]) == px and int(HT[i,2]) == py: #tile doesn't contain player
                        HT[i,3]="player"
                        HT[i,4]=DMG
                        HT[i,5]=HP
                        HT[i,6]=Team
                        
                        for k in range(0,TeamNumberTotal): # assign HT Allies
                            if k == 0:
                                for l in range(0,len(Team1)):
                                    if str(Team1[l]) == Team:
                                        HT[i,7]=1     
                            if k == 1:
                                for l in range(0,len(Team2)):
                                    if str(Team2[l]) == Team:
                                        HT[i,7]=2
                            if k == 2:
                                for l in range(0,len(Team3)):
                                    if str(Team3[l]) == Team:
                                        HT[i,7]=3
                            if k == 3:
                                for l in range(0,len(Team4)):
                                    if str(Team4[l]) == Team:
                                        HT[i,7]=4
                                    
                        
                        

                        
                        player.update(int(HT[i,1]),int(HT[i,2]))
                        print(HT)        
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseClick += 1
                      
    if mouseClick == 1:
        print("----")
        hasPlayer = False
        m = pygame.mouse.get_pos(0)
        mx = m[0]
        my = m[1]
        nx = math.floor((mx - 20)/ 30)       
        if nx%2 == 1:
            ny = math.floor((my - 15)/ 30)
        else:
            ny = math.floor((my-30)/ 30)
        
        hx = nx
        hy = ny
        playerMovementUpdate=True
        sprite_list.update(hx,hy,playerMovementUpdate,150,150,150) # color for selecting a tile
        sID = 1
        pygame.display.flip()
        mouseClick += 1
        if hasPlayer == False: #Resets to ready to be selected
            mouseClick = 0
            playerMovementUpdate=False
            sprite_list.update(hx,hy,playerMovementUpdate,0,0,255)
            sID = 1
            player.update(px, py)
            pygame.display.flip()

            
            
    elif mouseClick == 3 and hasPlayer == True:
        m = pygame.mouse.get_pos(0)
        mx = m[0]
        my = m[1]
        nx = math.floor((mx - 20)/ 30) 
        if nx%2 == 1:
            ny = math.floor((my - 15)/ 30)
        else:
            ny = math.floor((my-30)/ 30)
        #px3=px
        #py3=py
        px = nx
        py = ny

        if nx == hx and ny == hy:
            print("same")
            sameTile = True
        
        #Check for enemy
        
        for i in range(1,MapTNOT + 1):
            
            if int(HT[i,1]) == px and int(HT[i,2]) == py:
                if HT[i,3] == "player":
                    
                    
                    
                    
                    for j in range(1,MapTNOT + 1):
                        if int(HT[j,1]) == hx and int(HT[j,2]) == hy:

                            if (int(HT[j,1]) - int(HT[i,1])) <= 2 and (int(HT[j,2]) - int(HT[i,2])) <= 2: 
                                #in range
                                inRange = True
                                print("in range")
                            else:
                                #not in range
                                inRange = False
                                print("not in range")
                            
                            if int(HT[j,7]) == int(HT[i,7]): #Checks for ally or enemy
                                allies = True               #this happenes if they are allies

                            if allies == False and inRange == True:
                                
                                HT[j,3]="player"
                                mouseClick = 4
                                px2 = hx
                                py2 = hy
                                
                                HT[j,5]=int(HT[j,5])-int(HT[i,4]) #both damaging each other
                                HT[i,5]=int(HT[i,5])-int(HT[j,4])
                                
                                if int(HT[j,5]) <= 0:
                                    HT[j,3]="none"
                                    HT[j,4]="0"
                                    HT[j,6]="0"
                                    HT[j,7]="0"
                                    playerDead = True
                                if int(HT[i,5]) <= 0:
                                    HT[i,3]="none"
                                    HT[i,4]="0"
                                    HT[i,6]="0"
                                    HT[i,6]="0"
                                    playerDead = True
                            elif allies == True:
                                
                                allies = False
                                mouseClick = 0
                                playerMovementUpdate=False
                                sprite_list.update(hx,hy,playerMovementUpdate,0,0,255)
                                
                                HT[j,3]="player"
                                sID = 1
                                
                                player.update(hx, hy)
                                pygame.display.flip()
                                print(HT)
                                
                                
                                
                                
                                
                                
                    
                    
                
                    
                
        if mouseClick == 3:
            
            sprite_list.update(hx,hy,playerMovementUpdate,0,0,0)
            sID = 1
            
            player.update(px, py)
            mouseClick = 0
        elif mouseClick == 4:
            mouseClick = 0
            playerMovementUpdate=False
            sprite_list.update(hx,hy,playerMovementUpdate,0,0,255)
            sID = 1
            hasPlayer = False
            
            
            
            
            pygame.display.flip()
            playerDead = False

            for i in range(1,MapTNOT + 1):
                
                if HT[i,3]=="player":
                    
                    player.update(int(HT[i,1]),int( HT[i,2]))
                else:
                    sprite_list.update(int(HT[i,1]),int( HT[i,2]),playerMovementUpdate,0,0,255)
             
        print(HT)
        
        sameTile = False
    
    pygame.display.flip() #refresh screen
pygame.quit()
    
