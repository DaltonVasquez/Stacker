import sys
import pygame
import time
from block import Block

pygame.init()

BLOCK_SIZE = 25
MOVE_BLOCK_EVENT = 25     # ID number between 25 & 34

win_width = 16*BLOCK_SIZE
win_height = 20*BLOCK_SIZE

play_units_w = 7
play_units_h = 15
play_width = int(BLOCK_SIZE*play_units_w)
play_height = int(BLOCK_SIZE*play_units_h)
play_screen_x = int(win_width / 3)
play_posy = int(win_height/10)

BLOCK_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black
FOREGROUND_COLOR = (255, 255, 255)  # White

timer_init = time.time()
wait_time = .50
pygame.time.set_timer(MOVE_BLOCK_EVENT, 70)

block_pos = [play_screen_x, play_posy + play_height - BLOCK_SIZE]
num_blocks = 3

pygame.time.Clock()

screen = pygame.display.set_mode((win_width, win_height))

game_over = False


block_list[] =



def draw_play_area(frozen_blocks):
    #screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, FOREGROUND_COLOR, (play_screen_x, play_posy, play_width, play_height))
    for row in frozen_blocks:
        pygame.draw.rect(screen, BLOCK_COLOR, (block.freeze()))




 block_list[] =


while not game_over:

    draw_play_area(frozen_list)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                freeze_blocks(block_pos, num_blocks)
                block_pos[1] -= BLOCK_SIZE

        if pygame.event.get(MOVE_BLOCK_EVENT):  # check event queue contains
            #direction = move_block(direction)
    #time.sleep(wait_time)

    pygame.display.update()
    pygame.draw.rect(screen, BLOCK_COLOR, (block_pos[0], block_pos[1], BLOCK_SIZE*num_blocks, BLOCK_SIZE))