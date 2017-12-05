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
    instructions[position] += 1
    position += instruction
    steps += 1

print (steps)

