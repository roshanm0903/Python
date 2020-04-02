import pygame
pygame.init()

screen = pygame.display.set_mode([1000,500])  #create display , acts a surface

running = True
i=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((100,100,255))
    pygame.draw.circle(screen,(0,255,255),(500,250),i+100)
    pygame.draw.circle(screen,(0,0,255),(500,250),i)
    i+=1

    
    pygame.display.flip()  #push to display

pygame.quit()