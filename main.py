import pygame
from random import randint

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls")

GRAVITY = 9.8

class Ball(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (randint(0,255), randint(0,255), randint(0,255))


    def draw(self):
        pygame.draw.circle(screen, self.color ,(self.x, self.y),15,)

    def move(self):
        self.y += GRAVITY



# game loop
def game():
    running = True
    ball = Ball(20,20,20,20)
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.draw.line(screen, (255,255,255),(0,screen_height/3), (screen_width,screen_height/3),10)

        ball.draw()
        ball.move()
        pygame.display.update()

game()