#!/usr/bin/env python3

import sys
from itertools import combinations

with open(sys.argv[1], 'r') as input_file:
    quotients = []
    for line in input_file:
        nums = line.split()
        ints = list(map(int, nums))
        ints.sort(reverse=True)
        for dividend, divisor in combinations(ints, 2):
            if divisor == 0:
                continue
            if dividend % divisor == 0:
                quotients.append(dividend / divisor)
                break
    print(sum(quotients))
