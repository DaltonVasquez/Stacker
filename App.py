import sys
import pygame

pygame.init()

BLOCK_SIZE = 25

win_width = 16*BLOCK_SIZE
win_height = 20*BLOCK_SIZE

play_width = int(BLOCK_SIZE*7)
play_height = int(BLOCK_SIZE*15)
play_posx = int(win_width/3)
play_posy = int(win_height/10)

BLOCK_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black
FOREGROUND_COLOR = (255, 255, 255)  # White

block_start_pos = [play_posx, play_posy+play_height-BLOCK_SIZE]

pygame.time.Clock()

screen = pygame.display.set_mode((win_width, win_height))

game_over = False


def draw_play_area(frozen_blocks):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, FOREGROUND_COLOR, (play_posx, play_posy, play_width, play_height))
    # for x in frozen_blocks:
    #   pygame.draw.rect(screen, BLOCK_COLOR, (frozen_blocks[x][0], frozen_blocks[x][0], block_size, block_size))


while not game_over:

    draw_play_area(3)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block_start_pos[0] -= BLOCK_SIZE
            elif event.key == pygame.K_RIGHT:
                block_start_pos[0] += BLOCK_SIZE
        else:
            pass

    pygame.draw.rect(screen, BLOCK_COLOR, (block_start_pos[0], block_start_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()
