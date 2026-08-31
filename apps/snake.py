import curses
import random

def main(screen):
    curses.curs_set(0)
    screen.nodelay(1)
    screen.timeout(120)

    height, width = screen.getmaxyx()
    snake = [
        [height // 2, width // 4],
        [height // 2, width // 4 - 1],
        [height // 2, width // 4 - 2],
    ]

    direction = curses.KEY_RIGHT
    food = [height // 2, width // 2]
    screen.addch(food[0], food[1], curses.ACS_DIAMOND)
    score = 0

    while True:
        next_key = screen.getch()
        key = next_key if next_key != -1 else direction
        opposite = {
            curses.KEY_RIGHT: curses.KEY_LEFT,
            curses.KEY_LEFT: curses.KEY_RIGHT,
            curses.KEY_UP: curses.KEY_DOWN,
            curses.KEY_DOWN: curses.KEY_UP,
        }

        if key in opposite and key != opposite.get(direction):
            direction = key
        head = snake[0].copy()

        if direction == curses.KEY_RIGHT:
            head[1] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1
        snake.insert(0, head)

        hit_wall = head[0] in (0, height - 1) or head[1] in (0, width - 1)
        hit_self = head in snake[1:]
        if hit_wall or hit_self:
            break
        if head == food:
            score += 1
            food = None
            while food is None:
                candidate = [random.randint(1, height - 2), random.randint(1, width - 2)]
                if candidate not in snake:
                    food = candidate
            screen.addch(food[0], food[1], curses.ACS_DIAMOND)
        else:
            tail = snake.pop()
            screen.addch(tail[0], tail[1], " ")

        screen.addch(head[0], head[1], curses.ACS_CKBOARD)
        screen.addstr(0, 2, f" Score: {score} ")
        screen.refresh()

    screen.nodelay(0)
    screen.addstr(height // 2, width // 2 - 6, " GAME OVER ")
    screen.getch()

curses.wrapper(main)