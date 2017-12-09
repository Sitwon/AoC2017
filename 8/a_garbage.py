#!/usr/bin/env python3

import sys


level = 0
groups = []

in_garbage = False
in_bang = False

with open(sys.argv[1], 'r') as input_file:
    char = input_file.read(1)
    while char:
        if in_bang:
            in_bang = False
        elif in_garbage:
            if char == '>':
                in_garbage = False
            elif char == '!':
                in_bang = True
        else:
            if char == '<':
                in_garbage = True
            elif char == '{':
                level += 1
                groups.append(level)
            elif char == '}':
                level -= 1
        char = input_file.read(1)

print (sum(groups))
