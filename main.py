import pygame
from random import randint, uniform

# * Initialise game
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()
screen_width, screen_height = 1500, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls")
clock = pygame.time.Clock()

# * Game constants
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
GREY, LIGHT_GREY = (177,177,177), (100,100,100)
GRAVITY = 1
FPS = 60
BUTTON_SIZE=[screen_width//3, 100]


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
        # * Limit acceleration to only 2 to slow game down
        if self.ya < 2:
            self.yv = self.yv + self.ya
            self.ya += GRAVITY
            self.y = self.yv
        else:
            self.yv = self.yv + self.ya
            self.y += self.yv

        self.x += self.xv

    def x_collide(self):
        # * Handle collisions on sides
        self.xv *= -uniform(0.9, 1)
        self.xa *= -uniform(0.9, 1)
        self.bounces += 1

    def y_collide(self):
        # * Handle collisions on line
        self.yv *= -uniform(0.9, 1)
        self.xa *= -uniform(0.9, 1)
        self.bounces += 1

    def set_stationary(self):
        # todo implement ball rolling
        self.yv, self.ya = 0,0


# game loop
def game():
    running = True
    ball_radius = 15
    play = False
    txt = font.render("Random", True, (255,255,255))
    balls = [Ball(
                randint(ball_radius + 1, screen_width - ball_radius - 1), 
                randint(ball_radius + 1, screen_height - ball_radius - 1), 
                20, 20, ball_radius )  for _ in range(30)]

    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (screen_width//3 <= mouse[0] <= 2*screen_width//3) and (screen_height//6 <= mouse[1] <= screen_height//6 + BUTTON_SIZE[1]):
                    play = True
                # todo more buttons
        screen.fill(BLACK)

        if not play:
            # * Show game options
            if (screen_width//3 <= mouse[0] <= 2*screen_width//3) and (screen_height//6 <= mouse[1] <= screen_height//6 + BUTTON_SIZE[1]):
                pygame.draw.rect(screen, GREY, ((screen_width//3,screen_height//6), (BUTTON_SIZE[0],BUTTON_SIZE[1])))
            else:
                pygame.draw.rect(screen, LIGHT_GREY, ((screen_width//3,screen_height//6), (BUTTON_SIZE[0],BUTTON_SIZE[1])))
            screen.blit(txt,(200+screen_width//3, screen_height//6 + 25))
            # todo add more options
        
        else:
            # * Start game
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
            # todo implement rolling

        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    game()
