import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Warriors")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
player_img=pygame.image.load("spaceship.png")
playerX=360
playerY=480
def player():
    screen.blit(player_img,(playerX,playerY))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,255,0))
    player()
    pygame.display.update()       