#!/usr/bin/env python3

import sys


with open(sys.argv[1], 'r') as input_file:
    instructions = [
        int(line)
        for line in input_file
    ]

steps = 0
position = 0
instructions_len = len(instructions)
while (position >= 0) and (position < instructions_len):
    instruction = instructions[position]
    if instruction >= 3:
        instructions[position] -= 1
    else:
        instructions[position] += 1
    position += instruction
    steps += 1

print (steps)

