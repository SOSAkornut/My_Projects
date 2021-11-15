import pygame;
from pygame import mixer
import math
import threading


pygame.init();
icon = pygame.image.load("download.png")
pygame.display.set_caption("Sonic vs. Seelkadoom")
pygame.display.set_icon(icon)

pygame.mixer.music.load("seelkadoom_theme1.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((800*2, 200*3), pygame.RESIZABLE);

seelkadoom_hurt = pygame.mixer.Sound("seelkadoom_hurt.mp3")
punch = pygame.mixer.Sound("punch.mp3")
sonicX = 100
sonicY = 200
sonicImage = pygame.image.load("sonic_idle2.png")

backgroundSpeed = .01

punch_bool = False

seelkadoom_sound = False
seelkadoomImage = pygame.image.load("seelkadoom_idle2.png")
seelkadoomImage = pygame.transform.scale(seelkadoomImage, (140, 140))
seelkadoomX = 1400
seelkadoomY = 200
background = pygame.image.load("space2.jpg")
backgroundX = -105
running = True;

seelkadoom_speed = 10
sonic_speed = 10
sonic_attack = False
animation_idle = True

animation_attack1 = False
t = 0
n = 1
animation_t = 0

while running:
    animation_t += n
    screen.blit(background, (backgroundX, 0))
    
    screen.blit(seelkadoomImage, (seelkadoomX, seelkadoomY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
    t += 0.05;
    backgroundX -= backgroundSpeed
    if backgroundX < -325:
        backgroundX = -100

    if animation_idle == True:
        sonicImage = pygame.image.load("sonic_idle2 - Copy (2).png")
        sonicImage = pygame.image.load("sonic_idle2 - Copy (2).png")
    
        animation_idle = 2
    elif animation_idle == 2:
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")
        sonicImage = pygame.image.load("sonic_idle2.png")   
        animation_idle = True
    if animation_t > 1000:
        animation_attack1 = True
        
    if animation_attack1 == True:
        sonic_attack = True
        animation_idle = False
        animation_t = 0
        n = 0
        
        
        sonicX += sonic_speed+10
        sonicImage = pygame.image.load("sonic_dash.png")
        
        if punch_bool == True:
                seelkadoom_hurt.play()
                punch.play()
                punch_bool = False
               
                
        punch_bool = True
        if sonicX > (seelkadoomX - 500):
            sonic_speed = 0
            sonic_attack = False
            sonicX = 0
            sonicImage = pygame.image.load("sonic_aware.png")
            
            
            
    
            if sonicX < 100:
                sonic_speed = 0
                sonicX = 100
                
             
                animation_attack1 = 2
                seelkadoom_sound = True
                
                
     
      
           
       
        
    if animation_attack1 == 2:
        
        sonicX = 1300
        
        seelkadoomX = seelkadoomX + seelkadoom_speed

        if seelkadoomX > 20000:
            sonicImage = pygame.image.load("sonic_aware_inverted.png")
            seelkadoomImage = pygame.image.load("seelkadoom_idle_inverted.png")
            seelkadoom_speed = 0
            seelkadoomX = 100
            
            
            
                
            # stopped right here
            
            

        
        
    sonicY = (225 - math.sin(t/10) * (4+4))
    seelkadoomY = (225 - math.sin(t/10) * (6+6))
    
    screen.blit(sonicImage, (sonicX, sonicY))
    pygame.display.update()
    
pygame.quit();
