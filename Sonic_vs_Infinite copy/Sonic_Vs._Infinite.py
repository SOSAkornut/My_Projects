import pygame
from pygame import mixer
import time
import math
import random

pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Sonic vs Infinite")
icon = pygame.image.load("Sonic_life.png")
pygame.display.set_icon(icon)

infinite_damage = 1
background = pygame.image.load("CityBackground1.png")

PH_Ruby = pygame.image.load("PhantomRuby_cube.png")
backgroundX = -100
background_speed = -50

CubeX1 = 800
CubeY1 = random.uniform(0, 200)
CubeX1_change1 = 10
#CubeY_change = random.uniform(0, 100)

CubeX2 = 800
CubeY2 = random.uniform(0, 200)
CubeX2_change2 = 10
#CubeY2_change = random.uniform(0, 100)

CubeX3 = 800
CubeY3 = random.uniform(0, 200)
CubeX3_change3 = 10

sonic = pygame.image.load("Sonic.png")
infinite = pygame.image.load("Infinite.png")

sonic_jump = pygame.mixer.Sound("Sonic_Jump.mp3")
sonic_jump.set_volume(.1)

sonic_jump1 = pygame.mixer.Sound("Sonic_Jump.mp3")
sonic_jump1.set_volume(.5)

infinite_music = pygame.mixer.music.load("Infinite2_music copy.mp3")
pygame.mixer.music.play(-1)



sonic_health = 150

myfont = pygame.font.SysFont("Comic Sans MS", 30)
Sonic_text = myfont.render(f"Sonic: {sonic_health}", False, (0, 0, 250))

infinite_up = True
t = 1
sonicX = 200
sonicY = 492
sonicX_change = 0

infiniteX = 700
infiniteY = 292
infiniteY_change = .5
infinite_health = 5000

def platform1():
    pygame.draw.rect(screen, (25, 30, 25), (0, 550, 900, 400))

def platform2():
    pygame.draw.rect(screen, (200, 200, 200), (0, 550, 900, 10))

def Sonic(x, y):
    screen.blit(sonic, (x, y))

def Infinite(x, y):
    screen.blit(infinite, (x, y))

def Sonic_Live1(x, y, sonic):
    screen.blit(sonic, (x, y))

def Sonic_Live2(x, y, sonic):
    screen.blit(sonic, (x, y))

def Sonic_Live3(x, y, sonic):
    screen.blit(sonic, (x, y))     

def Cube1(x, y):
    screen.blit(PH_Ruby, (x, y))

def Cube2(x, y):
    screen.blit(PH_Ruby, (x, y))    

def Cube3(x, y):
    screen.blit(PH_Ruby, (x, y))
    
isJump = False
jumpCount = 18

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (backgroundX, -400))
    for event in pygame.event.get():

                 
        if event.type == pygame.QUIT:
            running = False
      
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sonicX_change += 5

                
            if event.key == pygame.K_SPACE:
                isJump = True
                sonic_jump1.play()
                sonic = pygame.image.load("sonic_ball.png")
                
         
             
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 sonicX_change -= 20
        
                
                
        if isJump == True:
            if jumpCount >= -18:
                sonicY -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 18
            else: # This will execute if our jump is finished
                jumpCount = 18
                isJump = False
                sonic = pygame.image.load("Sonic.png")
                                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                sonicX_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                sonicX_change = 0
       
            
    if sonicX > 710 and sonicY > infiniteY:
        sonicX = 400

    if sonicX < 0 :
        sonicX = 0
    
    if infinite_up:
        infiniteY -= infiniteY_change
   
    if infiniteY < 290:
        infinite_up = False
       
            
    t += 1/50
    infiniteY = 600/2 + math.sin(t) * 200
    

    distance = math.sqrt((infiniteX - sonicX)**2 + (sonicY - infiniteY)**2 )
        
    if distance < 100 and isJump == True:
        sonic_jump.play()
        infinite_health -= 6
        infinite = pygame.image.load("Infinite_hit.png")
        infinite_up = False
    
    if distance < 100 and isJump == False:
        sonic_health -= infinite_damage
    
        sonic_jump.play()
        sonic_jump.play()
        sonic_jump.play()
        sonic_jump.play()

    t += 1/50
    Sonic(sonicX, sonicY)
    Infinite(infiniteX, infiniteY)
    
    Cube1(CubeX1, CubeY1)

        
    Cube2(CubeX2, CubeY2+ 100)
    
        
    Cube3(CubeX3, CubeY3 + 200)

    if CubeX1 < 0:
        CubeX1 = 800
        CubeY1 = random.uniform(100, 600)
        CubeX1_change1 = 10

        CubeX2 = 800
        CubeY2 = random.uniform(100, 600)
        CubeX2_change2 = 10

        CubeX3 = 800
        CubeY3 = random.uniform(100, 600)
        CubeX3_change3 = 10
        
        Cube1(CubeX1 + 110, CubeY1 + 100)
        Cube2(CubeX2 + 100, CubeY2+ 400)      
        Cube3(CubeX3, CubeY3 + 200)
    
    platform1()
    platform2()
    if infinite_health < 4500:
        
        infiniteX = 800/2 + math.tan(t) * 60
        infiniteY = (600/2 + math.sin(t) * 60)

        CubeX1_change1 += .1
        
    if infinite_health < 4000:
        infiniteX = 800/2 + math.sin(t) * 200
        CubeX1_change1 = 16
        CubeX2_change2 = 14
        CubeX3_change3 = 18

    if infinite_health < 3500:
        infiniteX = (800/2 + math.cos(t*2) * 200)
        infiniteY =  (800/2 + math.tan(t*2) * 60)

    if infinite_health < 3000:
        infiniteX = (800/2 + math.cos(t) * 200)
        infiniteY =  (800/2 + math.sin(t) * 200)
        
    CubeX1 -= CubeX1_change1
    CubeX2 -= CubeX2_change2
    CubeX3 -= CubeX3_change3

    distance1 = math.sqrt((CubeX1 - sonicX)**2 + (sonicY -  CubeY1)**2)
    distance2 = math.sqrt((CubeX2 - sonicX)**2 + (sonicY -  CubeY2)**2)
    distance3 = math.sqrt((CubeX3 - sonicX)**2 + (sonicY -  CubeY3)**2)

    if distance1 <= 30:
        sonic_health -= .1
        sonicX -= 50
    
    if distance2 < 30:
        sonic_health -= .1
        sonicX -= 50

    if distance3 < 30:
        sonic_health -= .1
        sonicX -= 50
        
    sonicX += sonicX_change

    if sonic_health > 150:
        sonic_health = 150

    if sonic_health <= 0:
        running = False
        print("YOU DIED")
        

    myfont = pygame.font.SysFont("arialnarrow", 30)
    Sonic_text = myfont.render(f"Sonic: {sonic_health}", False, (100, 200, 239))

    myfont = pygame.font.SysFont("arialnarrow", 50)
    Infinite_text = myfont.render(f"Infinite: {infinite_health}", False, (250, 0, 0))

    screen.blit(Sonic_text, (0, 10))
    screen.blit(Infinite_text, (500, 10))

    sonic_health += 0.0035
    if infinite_up == False:
        infinite = pygame.image.load("Infinite.png")

    if infinite_health < 2500:

        if distance < 150 and isJump == False:
            sonic_health -= infinite_damage*2
    
            sonic_jump.play()
            sonic_jump.play()
            sonic_jump.play()
            sonic_jump.play()
            
        if distance < 150 and isJump == True:
            sonic_jump.play()
            infinite_health -= 1
            infinite = pygame.image.load("Infinite_hit.png")
            infinite_up = False
       
        infinite_damage = 2
        background = pygame.image.load("Infinite_Sky.png")
        infiniteX = (800/2 + math.cos(t*20) * (20))
        infiniteY =  (600/2 - math.sin(t*20) * (1))
        infiniteY_change = .1
        infinite = pygame.image.load("Infinite_stage2.png")
        
        
        Cube1(CubeX1 + 110, CubeY1 + 100)
        Cube2(CubeX2 + 100, CubeY2+ 400)      
        Cube3(CubeX3, CubeY3 + 200)

   
        
    if infinite_health < 2000:
        if distance < 150 and isJump == True:
            sonic_jump.play()
            infinite_health -= 1.5
            infinite = pygame.image.load("Infinite_hit.png")
            infinite_up = False
            
       
        infiniteX = (800/2 + math.cos(t*2) * (20))
        infiniteY = (600/2 - math.sin(t*2) * (20))

    if infinite_health <= 0:
        running = False
        print("YOU WON")


    if infinite_health < 1500:
        if distance < 150 and isJump == True:
            sonic_jump.play()
            infinite_health -= 1.5
            infinite = pygame.image.load("Infinite_hit.png")
            infinite_up = False
        
        infiniteX = (800/2 + math.cos(t) * (20))
        infiniteY = (600/2 - math.sin(t/5) * (20))
        

    if infinite_health < 1000:
        if distance < 150 and isJump == True:
            sonic_jump.play()
            infinite_health -= 1.5
            infinite = pygame.image.load("Infinite_hit.png")
            infinite_up = False
        
        infiniteX = (800/2 + math.cos(t*2) * 200)
        infiniteY =  (800/2 + math.sin(t*2) * 60)
        
    if infinite_health < 500:
        if distance < 150 and isJump == True:
            sonic_jump.play()
            infinite_health -= 1.5
            infinite = pygame.image.load("Infinite_hit.png")
            infinite_up = False
        
        infiniteX = (800/2 + math.cos(t/500) * (20))
        infiniteY = (600/2 - math.sin(t/50) * (20))
        

    
    if backgroundX < -800:
        backgroundX = -100

    backgroundX += background_speed
    pygame.display.update()
    pygame.display.flip()
            

pygame.quit()
