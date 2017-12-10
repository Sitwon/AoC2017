#!/usr/bin/env python3

import sys
import operator


nums = [
    n
    for n in range(256)
]

with open(sys.argv[1], 'r') as input_file:
    lengths = list(map(ord, list(input_file.readline().strip())))
    #lengths = list(map(ord, list('')))

lengths += [17, 31, 73, 47, 23]

cur_pos = 0
skip_size = 0

for i in range(64):
    for length in lengths:
        sub_nums = [nums[(cur_pos + pos) % 256] for pos in range(length)]
        sub_nums.reverse()
        for pos in range(length):
            nums[(cur_pos + pos) % 256] = sub_nums[pos]
        cur_pos += length
        cur_pos += skip_size
        skip_size += 1


dense_hash = []

while len(nums) > 0:
    digit = 0
    for i in nums[:16]:
        digit ^= i
    dense_hash.append(digit)
    nums = nums[16:]

hash_str = ''
for byte in dense_hash:
    hash_str += '%0.2x' % byte

print(hash_str)

