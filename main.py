import pygame
from random import randint, uniform

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls")
clock = pygame.time.Clock()

BLACK,WHITE = (0,0,0), (255,255,255)
GRAVITY = 1
FPS = 60

class Ball(object):
    def __init__(self, x, y, width, height,r):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.r = r
        self.yv = 0
        self.ya = 0

    def draw(self):
        pygame.draw.circle(screen, self.color ,(self.x, self.y),self.r)

    def move(self):
        if self.ya < 2:
            self.yv = self.yv + self.ya
            self.ya += GRAVITY
            self.y = self.yv
        else:
            self.yv = self.yv + self.ya
            self.y += self.yv

    def collide(self):
        self.yv = -uniform(0.5, 1)*self.yv

# game loop
def game():
    running = True
    balls = []
    for _ in range(15):
        balls.append(Ball(randint(0,800),randint(0,800),20,20,15))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)

        pygame.draw.line(screen, WHITE,(0,2*screen_height/3), (screen_width,2*screen_height/3),10)
        for ball in balls:
            if ball.y + ball.r > 2*screen_height/3 - 10:
                ball.collide()
            ball.draw()
            ball.move()

        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    game()