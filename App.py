import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
BACKGROUND_COLOR = (0,0,0) #Black

block_pos = [400,300]
block_size = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block_pos[0] -= block_size
            elif event.key == pygame.K_RIGHT:
                block_pos[0] += block_size
    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(screen, RED, (block_pos[0], block_pos[1], block_size, block_size))

    pygame.display.update()