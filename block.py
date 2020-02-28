class Block:

    def __init__(self, x_pos, y_pos, units):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = BLOCK_SIZE
        self.length = BLOCK_SIZE*units
        self.is_moving = True
        self.direction = 1  # 1 or -1

    def move_block(self):
        # if Block is at left boundary, go right
        if self.x_pos == play_screen_x:
            self.x_pos += BLOCK_SIZE
            self.direction = 1
        # if Block is at right boundary, go left
        elif self.x_pos == play_screen_x + play_width - BLOCK_SIZE*num_blocks:
            self.x_pos -= BLOCK_SIZE
            self.direction = -1
        else:
            self.x_pos = self.x_pos + self.direction*BLOCK_SIZE

    def freeze(self):
        self.is_moving = False
        return self.x_pos, self.y_pos, self.height, self.length
