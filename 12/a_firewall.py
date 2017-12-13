#!/usr/bin/env python3

import sys


firewall_scanners = {}
with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        depth, scan_range = map(int, line.split(': '))
        firewall_scanners[depth] = (0, scan_range, 0)

last_depth = depth

severity = 0

for i in range(last_depth + 1):
    if i in firewall_scanners.keys() and firewall_scanners[i][0] == 0:
        severity += i * firewall_scanners[i][1]
    for scanner in firewall_scanners.keys():
        this_scanner = firewall_scanners[scanner]
        if this_scanner[0] == 0:
            firewall_scanners[scanner] = (this_scanner[0] + 1, this_scanner[1], 0)
        elif this_scanner[0] == (this_scanner[1] - 1):
            firewall_scanners[scanner] = (this_scanner[0] - 1, this_scanner[1], 1)
        elif this_scanner[2] == 0:
            firewall_scanners[scanner] = (this_scanner[0] + 1, this_scanner[1], 0)
        else:
            firewall_scanners[scanner] = (this_scanner[0] - 1, this_scanner[1], 1)

print(severity)

