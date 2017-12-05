#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as input_file:
    diffs = []
    for line in input_file:
        nums = line.split()
        print('%r' % nums)
        ints = list(map(int, nums))
        print('%r' % ints)
        biggest = max(ints)
        smallest = min(ints)
        diffs.append(biggest - smallest)
    print(sum(diffs))
