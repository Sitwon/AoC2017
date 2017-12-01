#!/usr/bin/env python3

import re
import sys


input_string = sys.stdin.read()

ring_buff = [
    int(digit)
    for digit in input_string
    if re.match('\d', digit)
]

digits_to_add = []
for index, value in enumerate(ring_buff):
    if value == ring_buff[index - 1]:
        digits_to_add.append(value)

print(sum(digits_to_add))
