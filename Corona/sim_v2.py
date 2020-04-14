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

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

WINDOW_WIDTH = 460
WINDOW_HEIGHT = 460

REGION_WIDTH = 200
REGION_HEIGHT = 200

class Person(pygame.sprite.Sprite):
    def __init__(self):
        super(Person,self).__init__()
        self.surf = pygame.Surface((3,3))
        self.surf.fill((0,0,0))
        self.infected = False
        self.velocity = random.randint(0,2)
        self.theta = random.random()*math.pi*2
        self.immunity = random.randint(1,30)
        self.viremia = 0
        self.shed = 0  # need to model this - > how much would be transferred to others? percentage of viremias
        self.rect = self.surf.get_rect(
            center = (
                random.randint(20,WINDOW_WIDTH),
                random.randint(20,WINDOW_HEIGHT)
                )
            )
        self.region = 0   # 1-4 are restricted to some area, 5 no restrictions   
        self.origin_x = 40
        self.origin_y = 40
    def update(self):

        # position update
        self.theta += random.randint(-5,5)/100
        x = math.sin(self.theta)
        y = math.cos(self.theta)
        self.rect.move_ip(self.velocity*x, self.velocity*y)
        if self.region == 5:
            if self.rect.left < self.origin_x:
                self.rect.left = self.origin_x
                self.theta = random.random()*math.pi/2 
            if self.rect.right > WINDOW_WIDTH - self.origin_x :
                self.rect.right = WINDOW_WIDTH - self.origin_x
                self.theta = -random.random()*math.pi/2
            if self.rect.top <= self.origin_y:
                self.rect.top = self.origin_y
                self.theta = random.random()*math.pi/4
            if self.rect.bottom >= WINDOW_HEIGHT - self.origin_y :
                self.rect.bottom = WINDOW_HEIGHT - self.origin_y
                self.theta = random.random()*math.pi*3/4
        else:
                
            if self.rect.left < self.origin_x :
                self.rect.left = self.origin_x
                self.theta = math.pi/2
            if self.rect.right > REGION_WIDTH + self.origin_x  :
                self.rect.right = REGION_WIDTH + self.origin_x 
                self.theta = -math.pi/2
            if self.rect.top <= self.origin_y :
                self.rect.top =  self.origin_y
                self.theta = math.pi/4
            if self.rect.bottom >= REGION_HEIGHT+ self.origin_y  :
                self.rect.bottom =  REGION_HEIGHT+ self.origin_y
                self.theta = math.pi*3/4

        #viremia update
        self.shed = 0.1*self.viremia
        #infection update / color
        self.checkinfected()
        self.immunesystem()

    def immunesystem(self):

        if self.viremia > 20*self.immunity:    #hospitalized because of severe symptoms
            self.velocity = 0
            # pass
        elif self.viremia>self.immunity:
            self.viremia *= 1.1    #(1-1/10*(self.viremia - self.immunity))
        else:
            self.viremia -= self.immunity *0.8

    
    def checkinfected(self):
        if self.viremia > self.immunity:
            self.infected =True
            if self.viremia>1000:
                self.viremia =1000
            elif self.viremia<0:
                self.viremia = 0
            
            self.surf.fill((255,round(255 - self.viremia*255/1000),0))
            # self.surf.fill((255,0,0))
            infected_sprites.add(self)
            pop_sprites.remove(self)
                        
        else:
            self.infected = False 
            self.surf.fill((0,0,0))
            pop_sprites.add(self)
            infected_sprites.remove(self)




def population_gen(num,percentage,regions_infected):
    global pop 
    pop = [0] * num
    for i in range(num):
        pop[i]=Person()
        if i <= num/5:
            pop[i].region = 1
            # pop[i].origin_x = 40
            # pop[i].origin_y = 40
        elif i <= 2* num/5:
            pop[i].region = 2
            pop[i].origin_x += REGION_WIDTH + 20 
            # pop[i].origin_y = 40
        elif i <= 3* num/5:
            pop[i].region = 3
            # pop[i].origin_x = 40
            pop[i].origin_y += REGION_HEIGHT + 20
        elif i <= 4* num/5:
            pop[i].region = 4
            pop[i].origin_x += REGION_WIDTH + 20 
            pop[i].origin_y += REGION_HEIGHT + 20
        else:
            pop[i].region = 5
        pop_sprites.add(pop[i])

    for i in range( int(percentage*num/100) ):
        per = random.randint((4-regions_infected)*num/5,num) 
        pop[per].viremia = random.randint(1,1000)
        infected_sprites.add(pop[per])
        pop_sprites.remove(pop[per])
            

def transfer(carrier):
    for infec in pygame.sprite.spritecollide(carrier, pop_sprites, False):
        infec.viremia += carrier.shed
        infected_sprites.add(infec)
        pop_sprites.remove(infec)


pop =[]

pop_sprites = pygame.sprite.Group()    #pop that isnt infected
infected_sprites = pygame.sprite.Group()  #pop that is infected
population_gen(500,1,4)   #total population, percentage infected, number of regions of infection

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])  #create display , acts a surface
clock = pygame.time.Clock()

running = True
i=0


window = right_window = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

region1 = region2 = region3 = region4 = pygame.Surface((REGION_WIDTH, REGION_HEIGHT))
window.fill((240,240,240))
region1.fill((255,255,255))
region2.fill((255,255,255))
region3.fill((255,255,255))
region4.fill((255,255,255))

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pop_sprites.update()
    infected_sprites.update()

    screen.fill((80,80,255))

    # right_window.fill((255,255,255))

    screen.blit(window, (20,20))
    screen.blit(region1, (40,40))
    screen.blit(region2, (260,40))
    screen.blit(region3, (40,260))
    screen.blit(region4, (260,260))
    # screen.blit(right_window, (510,20))
    
    for per in infected_sprites:
        transfer(per) 

    for entity in pop_sprites:
        screen.blit(entity.surf, entity.rect)   #transfer one surface to another
    for entity in infected_sprites:
        screen.blit(entity.surf, entity.rect)   #transfer one surface to another
    
    pygame.display.flip()  #push to display
    clock.tick(1000)
    
    
pygame.quit()