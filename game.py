import pygame
import sys
import random

pygame.init()

width,height = 600,450
screen  = pygame.display.set_mode((width,height))
GRID_WIDTH ,GRID_HEIGHT = 30,30
run = True
def draw_grid():
    
    for i in range(0,height -1,GRID_HEIGHT):
        for j in range(0,width -1,GRID_WIDTH):
            grid_rect = pygame.Rect(j,i,GRID_WIDTH,GRID_HEIGHT)
            pygame.draw.rect(screen,(255,255,255),grid_rect,1)
            
class Snake():
    def __init__(self) -> None:
        self.x ,self.y = GRID_WIDTH,GRID_HEIGHT
        self.head = pygame.Rect(self.x,self.y,GRID_WIDTH,GRID_HEIGHT)
          
        self.col = (34,245,90)
        
        self.body = [pygame.Rect(self.x-GRID_WIDTH,self.y,GRID_WIDTH,GRID_HEIGHT)]
        self.dirx = 1
        self.diry = 0
    def draw(self):
        pass
    def update(self):
        
        self.body.append(self.head)
        
        for i in range(len(self.body)-1):
            self.body[i].x,self.body[i].y=self.body[i+1].x,self.body[i+1].y 
            
        self.head.x += self.dirx * GRID_WIDTH
        self.head.y += self.diry * GRID_WIDTH
        self.body.remove(self.head)
        

        if self.head.x >= width or self.head.x<0:
            self.head.x = GRID_WIDTH
            self.head.y = GRID_HEIGHT
        elif self.head.y >= height or self.head.y<0:
            self.head.x = GRID_WIDTH
            self.head.y = GRID_HEIGHT
            self.dirx = 1
            self.diry = 0

   
        


class Food():
    def __init__(self) -> None:
        self.x,self.y = random.randrange(30,width-GRID_WIDTH,GRID_WIDTH),random.randrange(30,height-GRID_HEIGHT,GRID_HEIGHT)
        self.food = pygame.Rect(self.x,self.y,GRID_WIDTH,GRID_HEIGHT)
        self.col = (234,45,90)
    def draw(self):
        pygame.draw.rect(screen,self.col,self.food)
snake = Snake()
food = Food()
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_w and snake.diry == 0:
                snake.dirx = 0
                snake.diry = -1
            elif event.key == pygame.K_s and snake.diry == 0:
                snake.dirx = 0
                snake.diry = 1
            elif event.key == pygame.K_d and snake.dirx == 0:
                snake.dirx = 1
                snake.diry = 0
            elif event.key == pygame.K_a and snake.dirx == 0:
                snake.dirx = -1
                snake.diry = 0
    
    snake.update()
    text = font.render(str(score), True,(20,20,255),(255,20,255))
    textRect = text.get_rect()
    textRect.center = ( width//2, 30)
    screen.fill((10,10,10))
    
    draw_grid()
    screen.blit(text, textRect)
    
    
    pygame.draw.rect(screen,(0,255,0),snake.head)
    for body in snake.body:
        pygame.draw.rect(screen,(0,255,0),body)
        if snake.head.colliderect(food.food):
            snake.body.append(pygame.Rect(body.x,body.y,GRID_WIDTH,GRID_HEIGHT))
            score +=1
            food = Food()
        if snake.head.colliderect(body):
            snake = Snake()
            food = Food()
            score = 0
    food.draw()
    pygame.display.update()
    clock.tick(10)



