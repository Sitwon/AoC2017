#!/usr/bin/env python3

import sys

position = int(sys.argv[1])

ring = 1
while ring ** 2 < position:
    ring += 2

square = ring ** 2
ring_distance = int((ring - 1) / 2)
south = int((square + (square - (ring - 1))) / 2)
west = int(((square - (ring - 1)) + (square - ((ring - 1) * 2))) / 2)
north = int(((square - ((ring - 1) * 2)) + (square - ((ring - 1) * 3))) / 2)
east = int(((square - ((ring - 1) * 3)) + (square - ((ring - 1) * 4))) / 2)

print (ring_distance, ring, square, south, west, north, east)
dists=[
    abs(position - middle)
    for middle in [south, west, north, east]
]
print (dists)
laterall_dist = min(dists)
print (laterall_dist)
print (laterall_dist + ring_distance)
