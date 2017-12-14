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
    list(bin(int(knot_hash('%s-%d' % (puzzle_input, i)), 16))[2:].zfill(128))
    for i in range(128)
]

regions = [
    [0 for i in range(128)]
    for j in range(128)
]


def check_neighbors(row, col, region, hashes, regions):
    if row > 127 or row < 0 or col > 127 or col < 0:
        return
    if regions[row][col]:
        return
    if hashes[row][col] == '0':
        return
    regions[row][col] = region_count
    check_neighbors(row + 1, col, region, hashes, regions)
    check_neighbors(row - 1, col, region, hashes, regions)
    check_neighbors(row, col + 1, region, hashes, regions)
    check_neighbors(row, col - 1, region, hashes, regions)




region_count = 0
for row in range(128):
    for box in range(128):
        if regions[row][box] != 0:
            continue
        if hashes[row][box] == '0':
            continue
        region_count += 1
        check_neighbors(row, box, region_count, hashes, regions)

print(region_count)
