import pygame
from random import randint, uniform, seed

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls")
clock = pygame.time.Clock()

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
GRAVITY = 1
FPS = 60


class Ball(object):
    def __init__(self, x, y, width, height, r):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.r = r
        self.yv = 0
        self.ya = 0
        self.xa = 0
        self.xv = randint(1,10)
        self.bounces = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        if self.ya < 2:
            self.yv = self.yv + self.ya
            self.ya += GRAVITY
            self.y = self.yv
        else:
            self.yv = self.yv + self.ya
            self.y += self.yv

        self.x += self.xv

    def x_collide(self):
        self.xv *= -uniform(0.9, 1)
        self.xa *= -uniform(0.9, 1)
        self.bounces += 1

    def y_collide(self):
        self.yv *= -uniform(0.9, 1)
        self.xa *= -uniform(0.9, 1)
        self.bounces += 1

    def set_stationary(self):
        self.yv, self.ya = 0,0


# game loop
def game():
    running = True
    ball_radius = 15
    balls = [ Ball(
                randint(ball_radius + 1, screen_width - ball_radius - 1), 
                randint(ball_radius + 1, screen_height - ball_radius - 1), 
                20, 20, ball_radius )  for _ in range(30)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)

        line_y = int(2 * screen_height / 3) - 10
        line_width = 10
        pygame.draw.line(screen, WHITE, (0, line_y), (screen_width, line_y), line_width)

        for ball in balls:
            if(ball.x - ball.r <= 0) or (ball.x + ball.r >= screen_width):
                ball.x_collide()
            elif  (ball.y + ball.r >= line_y):
                ball.y_collide()
            ball.move()
            ball.draw()

        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    game()
