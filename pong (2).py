import pygame
import random
from sys import exit

em = -60

pygame.init()
screen = pygame.display.set_mode((1200,700))
clock = pygame.time.Clock()

Background = pygame.Surface((1200,700))
Background.fill((0,0,0))

block_font = pygame.font.Font(r"C:\Users\Marion\Downloads\BlockStockRegular-A71p.ttf", 30)

x = 75
y = 350
a = 1125
b = 350
v = 600
m = 350
rp = 0
lp = 0
rp = 0

xdp = True
yd = random.randrange(-3,3)

Lup = 0
Ldown= 0
Rup = 0
Rdown = 0

left_paddle = pygame.Surface((10,60))
left_paddle.fill((255,255,255))

leftp = block_font.render(str(lp),True,30)
rightp = block_font.render(str(rp),False,30)

right_paddle = pygame.Surface((10,60))
right_paddle.fill((255,255,255))

ball = pygame.Surface((20,20))
ball.fill((255,255,255))

begin = True

while True:
    pygame.display.update()
    left_rect = left_paddle.get_rect(center=(x, y))
    right_rect = right_paddle.get_rect(center=(a,b))
    ball_rect = ball.get_rect(center=(v,m))
    dt = clock.tick(400)/100*80
    leftp = block_font.render(str(lp),False,(255,255,255))
    lpl = leftp.get_rect(center=(300, 50))
    rightp = block_font.render(str(rp), False, (255,255,255))
    rpl = rightp.get_rect(center = (900,59))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Lup = 1
            if event.key == pygame.K_s:
                Ldown = 1
            if event.key == pygame.K_UP:
                Rup = 1
            if event.key == pygame.K_DOWN:
                Rdown = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Lup = 0
            if event.key == pygame.K_s:
                Ldown = 0
            if event.key == pygame.K_UP:
                Rup = 0
            if event.key == pygame.K_DOWN:
                Rdown = 0
    
    screen.blit(Background, (0,0))
    screen.blit(left_paddle,left_rect)
    screen.blit(left_paddle,right_rect)
    screen.blit(ball,ball_rect)
    screen.blit(leftp, lpl)
    screen.blit(rightp,rpl)

    if ball_rect.colliderect(left_rect):
        xdp = True
        yd = random.randrange(-3, 3)
    if ball_rect.colliderect(right_rect):
        xdp = False
        yd = random.randrange(-3, 3)

    if Lup == 1:
        y -= dt
    if Ldown == 1:
        y += dt
    if Rup == 1:
        b -= dt
    if Rdown == 1:
        b += dt

    if y <= 30:
        y=  30
    if y >= 670:
        y = 670
    if b <= 30:
        b=  30
    if b >= 670:
        b = 670
    if xdp == True:
        v += dt/3
        if yd == 0:
            v += dt/3
    if xdp == False:
        v -= dt/3
        if yd == 0:
            v += dt/3
    if m <= 20:
        yd = yd - (yd*2)
    if m >= 700:
        yd = yd - (yd*2)
    if v <= 0:
        rp += 1
        begin = True
    if v >= 1200:
        lp += 1
        begin = True
    if begin == True:
        tt = 0
        while True:
            dt = clock.tick()
            tt += dt
            pygame.display.update()
            left_rect = left_paddle.get_rect(center=(x, y))
            right_rect = right_paddle.get_rect(center=(a, b))
            ball_rect = ball.get_rect(center=(v, m))
            screen.blit(Background, (0, 0))
            screen.blit(left_paddle, left_rect)
            screen.blit(left_paddle, right_rect)
            screen.blit(ball, ball_rect)
            screen.blit(leftp, lpl)
            screen.blit(rightp, rpl)
            v = 600
            m = 350
            if tt >= 1000:
                begin = False
                break

    m += yd