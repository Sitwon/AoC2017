#!/usr/bin/env python3

import re
import sys


input_string = sys.stdin.read()

ring_buff = [
    int(digit)
    for digit in input_string
    if re.match('\d', digit)
]

ring_buff_len = len(ring_buff)
halfway = int(ring_buff_len / 2)

digits_to_add = []
for index, value in enumerate(ring_buff):
    test_index = index + halfway
    if test_index >= ring_buff_len:
        test_index -= ring_buff_len
    if value == ring_buff[test_index]:
        digits_to_add.append(value)

print(sum(digits_to_add))
