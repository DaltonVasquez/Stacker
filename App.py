import sys
import pygame
import time

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

timer_init = time.time()
wait_time = .50

block_pos = [play_posx, play_posy + play_height - BLOCK_SIZE]
num_blocks = 3
direction = 1

pygame.time.Clock()

screen = pygame.display.set_mode((win_width, win_height))

game_over = False

frozen_list = []


def freeze_blocks(pos, block_count):
    frozen_list.append([pos[0],pos[1],block_count])
    print(frozen_list)


def draw_play_area(frozen_blocks):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, FOREGROUND_COLOR, (play_posx, play_posy, play_width, play_height))
    for row in frozen_blocks:
        pygame.draw.rect(screen, BLOCK_COLOR, (row[0], row[1], BLOCK_SIZE*(row[2]), BLOCK_SIZE))


while not game_over:

    draw_play_area(frozen_list)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                freeze_blocks(block_pos,num_blocks)
                block_pos[1] -= BLOCK_SIZE

    time.sleep(wait_time)
    if block_pos[0] == play_posx:
        block_pos[0] += BLOCK_SIZE
        direction = 1
    elif block_pos[0] == play_posx + play_width - BLOCK_SIZE*num_blocks:
        block_pos[0] -= BLOCK_SIZE
        direction = -1
    else:
        block_pos[0] = block_pos[0] + direction*BLOCK_SIZE


    pygame.draw.rect(screen, BLOCK_COLOR, (block_pos[0], block_pos[1], BLOCK_SIZE*num_blocks, BLOCK_SIZE))

    pygame.display.update()
