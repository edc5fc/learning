import pygame
pygame.init()
boardwidth = 1000
boardheight = 500
win=pygame.display.set_mode((boardwidth, boardheight))

pygame.display.set_caption("game 1")

x=60
y=60
width=40
height=60
vel=7
jump=False
countJ=10

run=True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT]and x < boardwidth - width - vel:
        x += vel
    if not(jump):
        if keys[pygame.K_UP]and y>vel:
           y-=vel
        if keys[pygame.K_DOWN]and y<500-height-vel:
           y+=vel
        if keys[pygame.K_SPACE]:
            jump=True
    else:
        if countJ>=-10:
          neg=1
          if countJ<0:
              neg=-1
        
          y-=(countJ**2)*0.5*neg
          countJ-=1
        else:
            jump=False
            countJ=10
    win.fill((0,0,0)) 
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
                     
    

pygame.quit()

