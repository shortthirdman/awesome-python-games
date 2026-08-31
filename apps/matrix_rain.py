import random

from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

CHARACTERS = "アカサタナハマヤラワ0123456789ABCDEFXYZ#$%&"

def matrix_rain(screen):
    height = screen.height
    width = screen.width
    drop_positions = [random.randint(-height, 0) for _ in range(width)]
    drop_speeds = [random.randint(1, 3) for _ in range(width)]
    frame_count = 0
    while True:
        for column in range(width):
            char = random.choice(CHARACTERS)
            row = drop_positions[column]
            if 0 <= row < height:
                screen.print_at(char, column, row, colour=Screen.COLOUR_GREEN, bg=Screen.COLOUR_BLACK)
            trail_row = row - 1
            if 0 <= trail_row < height:
                trail_char = random.choice(CHARACTERS)
                screen.print_at(trail_char, column, trail_row, colour=Screen.COLOUR_WHITE, bg=Screen.COLOUR_BLACK)
            fade_row = row - 6
            if 0 <= fade_row < height:
                screen.print_at(" ", column, fade_row)
            drop_positions[column] += drop_speeds[column]
            if drop_positions[column] > height + 6:
                drop_positions[column] = random.randint(-20, 0)
                drop_speeds[column] = random.randint(1, 3)
        frame_count += 1
        event = screen.get_key()
        if event in (ord("q"), ord("Q")):
            return
        screen.refresh()
        screen.wait_for_input(0.05)

while True:
    try:
        Screen.wrapper(matrix_rain)
        break
    except ResizeScreenError:
        pass