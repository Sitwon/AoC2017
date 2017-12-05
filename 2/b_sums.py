#!/usr/bin/env python

import sys

target = int(sys.argv[1])


grid = [
    [0 for _ in range(101)]
    for _ in range(101)
]

pos = (50, 50)

def value_at(grid, pos):
    return grid[pos[0]][pos[1]]

def value_s(grid, pos):
    return grid[pos[0]][pos[1]-1]

def value_n(grid, pos):
    return grid[pos[0]][pos[1]+1]

def value_w(grid, pos):
    return grid[pos[0]-1][pos[1]]

def value_e(grid, pos):
    return grid[pos[0]+1][pos[1]]

def value_ne(grid, pos):
    return grid[pos[0]+1][pos[1]+1]

def value_nw(grid, pos):
    return grid[pos[0]-1][pos[1]+1]

def value_se(grid, pos):
    return grid[pos[0]+1][pos[1]-1]

def value_sw(grid, pos):
    return grid[pos[0]-1][pos[1]-1]

def pos_sum(grid, pos):
    nums = (
        value_n(grid, pos),
        value_s(grid, pos),
        value_e(grid, pos),
        value_w(grid, pos),
        value_ne(grid, pos),
        value_nw(grid, pos),
        value_se(grid, pos),
        value_sw(grid, pos),
    )
    #print ('%r' % (nums,))
    return sum(nums)

def set_value(grid, pos, val):
    grid[pos[0]][pos[1]] = val


def move(pos, facing):
    if facing == 'E':
        return (pos[0]+1, pos[1])
    if facing == 'W':
        return (pos[0]-1, pos[1])
    if facing == 'N':
        return (pos[0], pos[1]+1)
    if facing == 'S':
        return (pos[0], pos[1]-1)

def turn(facing):
    if facing == 'E':
        return 'N'
    if facing == 'N':
        return 'W'
    if facing == 'W':
        return 'S'
    if facing == 'S':
        return 'E'

current_number = 1
set_value(grid, pos, current_number)

journey = []
step = 0
facing = 'E'
#print('%r %r' % (pos, current_number))
while current_number < target:
    step += 1
    pos = move(pos, facing)

    if len(journey) < 2:
        journey.append(step)
        facing = turn(facing)
        step = 0
    elif journey[-1] == journey[-2] and journey[-1] < step:
        journey.append(step)
        facing = turn(facing)
        step = 0
    elif journey[-1] != journey[-2] and journey[-1] == step:
        journey.append(step)
        facing = turn(facing)
        step = 0

    current_number = pos_sum(grid, pos)
    #print('%r %r' % (pos, current_number))
    set_value(grid, pos, current_number)

print (current_number)
