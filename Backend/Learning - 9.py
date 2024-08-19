import pygame
import random

# Pygame'ni ishga tushirish
pygame.init()

# Ekran o'lchami
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Ranglar
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Ball'ning o'lchami va boshlang'ich joylashuvi
ball_size = 20
ball_x = screen_width // 2
ball_y = screen_height // 2

# Ball'ning tezligi
ball_speed_x = random.choice([-5, 5])
ball_speed_y = random.choice([-5, 5])

# O'yin loop'i
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ball'ni harakatlantirish
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Devorga tegib qaytish
    if ball_x <= 0 or ball_x >= screen_width - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y = -ball_speed_y

    # Ekranni tozalash
    screen.fill(black)

    # Ball'ni chizish
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_size)

    # Ekranni yangilash
    pygame.display.flip()

    # O'yinni sekinlashtirish
    pygame.time.Clock().tick(60)

# Pygame'ni yopish
pygame.quit()
