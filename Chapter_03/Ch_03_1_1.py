import curses
import time

TERMINAL = 1

# Use right hand wall method
MAZE_SIZE = 19
ROBOT = "*"

UP = 1
RIGHT = 2
DOWN = 4
LEFT = 8

rec = []


def get_shape(m, x, y):
    shape = (u' ', u'\u2502', u'\u2500', u'\u2514', u'\u2502', u'\u2502', u'\u250c', u'\u251c', u'\u2500', u'\u2518',
             u'\u2500', u'\u2534', u'\u2510', u'\u2524', u'\u252c', u'\u253c')
    s = 0
    if m[x][y] != 0:
        # Check upper range
        if x > 0 and m[x-1][y] != 0:
            s |= UP
        # Check lower range
        if x < MAZE_SIZE - 2 and m[x+1][y] != 0:
            s |= DOWN
        # Check left range
        if y > 0 and m[x][y-1] != 0:
            s |= LEFT
        # Check right range
        if y < MAZE_SIZE - 2 and m[x][y+1] != 0:
            s |= RIGHT
    return shape[s]


def draw_maze(m):
    for j in range(MAZE_SIZE):
        for i in range(MAZE_SIZE):
            ch = get_shape(m, i, j)
            if TERMINAL:
                stdscr.addstr(i+1, 2*(j+1), ch)
                stdscr.refresh()


def record(x, y):
    rec.append(x)
    rec.append(y)


def forward(x, y, dir):
    # Delete mouse
    if TERMINAL:
        stdscr.addstr(x + 1, 2*(y + 1), " ")
        stdscr.refresh()

    if dir == LEFT:
        y -= 1
    if dir == RIGHT:
        y += 1
    if dir == UP:
        x -= 1
    if dir == DOWN:
        x += 1

    # Record movement of mouse
    record(x, y)

    # Draw mouse
    if TERMINAL:
        stdscr.addstr(x + 1, 2*(y + 1), ROBOT)
        stdscr.refresh()

    return x, y


def still_in_maze(x, y):
    if 0 < x < MAZE_SIZE - 1 and 0 < y < MAZE_SIZE -1:
        return True
    else:
        return False


def wall_ahead(m, x, y, dir):
    if dir == LEFT:
        y -= 1
    if dir == RIGHT:
        y += 1
    if dir == UP:
        x -= 1
    if dir == DOWN:
        x += 1

    return m[x][y]


def right(dir):
    dir <<= 1
    if dir > LEFT:
        dir = UP

    return dir


def left(dir):
    dir >>= 1
    if dir == 0:
        dir = LEFT

    return dir


def right_hand(m, x, y, dir):
    if TERMINAL:
        stdscr.addstr(x + 1, 2*(y + 1), ROBOT)
        stdscr.refresh()
    time.sleep(0.1)
    # Record movement of mouse
    record(x, y)
    x, y = forward(x, y, dir)
    while still_in_maze(x, y):
        # 100 ms sleep
        time.sleep(0.1)
        dir = right(dir)
        while wall_ahead(m, x, y, dir):
            dir = left(dir)
        x, y = forward(x, y, dir)
    # End of record
    record(-1, -1)


# Main routine
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

if TERMINAL:
    stdscr = curses.initscr()
    # Clear screen
    stdscr.clear()

draw_maze(maze)
right_hand(maze, MAZE_SIZE-2, MAZE_SIZE-1, LEFT)

if TERMINAL:
    stdscr.getkey()
