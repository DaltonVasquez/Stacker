import sys
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 850

BLOCK_COLOR = (255,0,0)             #Red
BACKGROUND_COLOR = (0,0,0)          #Black
FOREGROUND_COLOR = (255,255,255)    #White

block_pos = [400,300]
block_size = 50

pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

def draw_play_area(frozen_blocks):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, FOREGROUND_COLOR, (150, 50, 7*50, 15*50))
    for x,y in frozen_blocks:
        pygame.draw.rect(screen, BLOCK_COLOR, (frozen_blocks[x][0], frozen_blocks[y][0], block_size, block_size))


while not game_over:

    draw_play_area(3)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block_pos[0] -= block_size
            elif event.key == pygame.K_RIGHT:
                block_pos[0] += block_size
        else:
            pass

    pygame.draw.rect(screen, BLOCK_COLOR, (block_pos[0], block_pos[1], block_size, block_size))

    pygame.display.update()