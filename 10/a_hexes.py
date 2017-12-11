#!/usr/bin/env python3

import sys


def read_steps(input_file):
    step = ''
    while True:
        read_buffer = input_file.read()
        while read_buffer != '':
            char = read_buffer[0]
            read_buffer = read_buffer[1:]
            if char == '\n':
                continue
            if char == ',':
                yield step
                step = ''
            else:
                step += char
        if step != '':
            yield step
        break

position = (0, 0, 0)

with open(sys.argv[1], 'r') as input_file:
    for step in read_steps(input_file):
        if step == 'n':
            x = position[0]
            y = position[1] + 1
            position = (x, y, 0 - (x + y))
        elif step == 's':
            x = position[0]
            y = position[1] - 1
            position = (x, y, 0 - (x + y))
        elif step == 'nw':
            x = position[0] - 1
            y = position[1] + 1
            position = (x, y, 0 - (x + y))
        elif step == 'ne':
            x = position[0] + 1
            y = position[1]
            position = (x, y, 0 - (x + y))
        elif step == 'sw':
            x = position[0] - 1
            y = position[1]
            position = (x, y, 0 - (x + y))
        elif step == 'se':
            x = position[0] + 1
            y = position[1] - 1
            position = (x, y, 0 - (x + y))

distance = max(map(abs, list(position)))
print(distance)
