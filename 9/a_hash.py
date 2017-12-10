#!/usr/bin/env python3

import sys


nums = [
    n
    for n in range(256)
]

with open(sys.argv[1], 'r') as input_file:
    lengths = map(int, input_file.readline().split(','))

cur_pos = 0
skip_size = 0

for length in lengths:
    sub_nums = [nums[(cur_pos + pos) % 256] for pos in range(length)]
    sub_nums.reverse()
    for pos in range(length):
        nums[(cur_pos + pos) % 256] = sub_nums[pos]
    cur_pos += length
    cur_pos += skip_size
    skip_size += 1

print (nums[0] * nums[1])
