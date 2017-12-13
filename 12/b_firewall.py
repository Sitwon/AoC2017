#!/usr/bin/env python3

import sys


def increment_scanners(firewall_scanners):
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
    return firewall_scanners

firewall_scanners = {}
with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        depth, scan_range = map(int, line.split(': '))
        firewall_scanners[depth] = (0, scan_range, 0)

last_depth = depth

delay = 0
packets = []
answer = False

while True:
    packets.append([delay, 0])
    packets = [
        [packet[0], packet[1] + 1]
        for packet in packets
        if packet[1] not in firewall_scanners.keys() or firewall_scanners[packet[1]][0] != 0
    ]
    for packet in packets:
        if packet[1] > last_depth:
            answer = packet[0]
            break
    if answer:
        break

    delay += 1
    increment_scanners(firewall_scanners)

print(answer)

