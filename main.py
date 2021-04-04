import pygame, sys, random
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()

class Ball():
    def __init__(self):
        self.size = 20
        self.color_white = white
        self.color_grey = grey
        self.ball = pygame.Rect(screen_width / 2 - self.size / 2, screen_height / 2 - self.size / 2, self.size, self.size )
        self.ball_speed = (random.choice((5,-5)), 5)
        self.ball_speed = list(self.ball_speed)
        self.slope = None

    def render(self,screen,pos):
        pygame.draw.ellipse(screen, self.color_white, self.ball, 2)
        self.ball.move_ip(self.ball_speed)
        if self.ball.left < 0:
            self.ball_speed[0] *= -1
        if self.ball.right > screen_width:
            self.ball_speed[0] *= -1
        if self.ball.top < 30:
            self.ball_speed[1] *= -1
        if self.ball.bottom > screen_height:
            self.ball_speed[1] *= -1

        if self.ball.colliderect(pos):
            self.ball_speed[1] *= -1
        if self.ball.bottom == pos[1]:
            if pos[0] > self.ball.left < pos[0] + 10:
                print(pos[1])



class Platform():
    def __init__(self):
        self.size = (110, 10)
        self.color = white
        self.move_speed = 8
        self.platform = pygame.Rect((screen_width / 2) - self.size[0], (screen_height - 10) - self.size[1], self.size[0], self.size[1])

    def render(self,screen):
        pygame.draw.rect(screen, self.color, self.platform, 1)


    def movement(self,l,r):
        if move_left:
            self.platform.move_ip(-self.move_speed,0)
        if move_right:
            self.platform.move_ip(self.move_speed,0)
        if self.platform.left < 0:
            self.platform[0] = 0
        if self.platform.right > screen_width:
            self.platform[0] = screen_width - self.size[0]




#color
white = (255,255,255)
grey = (100,100,100)
#screen
screen_width = 440
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Game')

ball = Ball()
platform = Platform()

font = pygame.font.SysFont(None,24)

lives = 5
move_left = False
move_right = False


while True:
    screen.fill((0,0,0))
    pygame.draw.line(screen,white,(0,30),(screen_width,30))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_left = True
            elif event.key == K_RIGHT:
                move_right = True
        else:
            move_left = False
            move_right = False



    #platform
    platform.movement(move_left, move_right)
    platform.render(screen)
    platfrom_pos = platform.platform
    #ball
    ball.render(screen,platfrom_pos)

    #fps
    fps_d = int(clock.get_fps())
    fps = font.render(str(fps_d),True,(255,255,0))
    screen.blit(fps,(screen_width - 30 ,0))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
