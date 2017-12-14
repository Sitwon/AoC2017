#!/usr/bin/env python3

import sys


def knot_hash(input_str):
    nums = [
        n
        for n in range(256)
    ]

    lengths = list(map(ord, list(input_str)))

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

    return hash_str


with open(sys.argv[1], 'r') as input_file:
    puzzle_input = input_file.read().strip()

#puzzle_input = 'flqrgnkx'

hashes = [
    repr(bin(int(knot_hash('%s-%d' % (puzzle_input, i)), 16)))[2:]
    for i in range(128)
]

print(sum([bin_str.count('1') for bin_str in hashes]))

