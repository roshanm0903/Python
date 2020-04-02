import pygame
import random
import math

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

WINDOW_WIDTH = 470
WINDOW_HEIGHT = 460

class Person(pygame.sprite.Sprite):
    def __init__(self):
        super(Person,self).__init__()
        self.surf = pygame.Surface((3,3))
        self.surf.fill((0,0,0))
        self.infected = False
        self.velocity = random.randint(1,2)
        self.theta = random.random()*math.pi*2
        self.immunity = random.randint(1,30)
        self.viremia = 0
        self.shed = 1  # need to model this - > how much would be transferred to others? percentage of viremias
        self.rect = self.surf.get_rect(
            center = (
                random.randint(20,WINDOW_WIDTH),
                random.randint(20,WINDOW_HEIGHT)
                )
            )

    def update(self):

        # position update
        self.theta += random.randint(-5,5)/100
        x = math.sin(self.theta)
        y = math.cos(self.theta)
        self.rect.move_ip(self.velocity*x, self.velocity*y)

        if self.rect.left < 20:
            self.rect.left = 20
            self.theta = math.pi/2
        if self.rect.right > WINDOW_WIDTH + 20 :
            self.rect.right = WINDOW_WIDTH + 20
            self.theta = -math.pi/2
        if self.rect.top <= 20:
            self.rect.top = 20
            self.theta = math.pi/4
        if self.rect.bottom >= WINDOW_HEIGHT +20 :
            self.rect.bottom = WINDOW_HEIGHT +20
            self.theta = math.pi*3/4
        #viremia update

        #infection update / color
        if self.viremia > 10:
            self.infected = True
        else:
            self.infected = False
            infected_sprites.remove(self)

        if self.infected:
            if self.viremia>100:
                self.viremia =100
            elif self.viremia<0:
                self.viremia = 0
            self.surf.fill((255,255 - self.viremia*255/100,255 - self.viremia*255/100))
            self.shed = 0.1*self.viremia
            # pass
    
    def checkinfected(self):
        if self.viremia > self.immunity:
            self.infected =True
        else:
            self.infected = False 
            self.surf.fill((0,0,0))

pop =[]

def population_gen(num,percentage):
    global pop 
    pop = [0] * num
    for i in range(num):
        pop[i]=Person()
        if i <= percentage*num/100:
            pop[i].infected=True
            pop[i].viremia = random.randint(1,100)
            infected_sprites.add(pop[i])

        pop_sprites.add(pop[i])


def transfer(carrier,contacts):
    for infec in pygame.sprite.spritecollide(carrier, contacts, False):
        infec.infected = True
        infec.viremia += carrier.shed
        infected_sprites.add(infec)
        

pop_sprites = pygame.sprite.Group()
infected_sprites = pygame.sprite.Group()
population_gen(500,1)

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])  #create display , acts a surface
clock = pygame.time.Clock()

running = True
i=0

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pop_sprites.update()
    screen.fill((80,80,255))
    left_window = right_window = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    left_window.fill((255,255,255))
    right_window.fill((255,255,255))
    
    screen.blit(left_window, (20,20))
    screen.blit(right_window, (510,20))
    
    for per in infected_sprites:
        transfer(per,pop_sprites) 
        # print("additional person")
        # for infec in pygame.sprite.spritecollide(per, pop_sprites, False):
        #     infec.infected = True
        #     #add infected to infected group
        #     infected_sprites.add(infec)

    for entity in pop_sprites:
        screen.blit(entity.surf, entity.rect)   #transfer one surface to another
    pygame.display.flip()  #push to display
    clock.tick(60)
    
    
pygame.quit()