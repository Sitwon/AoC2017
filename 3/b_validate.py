#!/usr/bin/env python3

import sys

valid = 0

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        words = line.split()
        words = [''.join(sorted(word)) for word in words]
        if len(words) == len(set(words)):
            valid += 1

print (valid)

