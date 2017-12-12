#!/usr/bin/env python3

import sys


pid_pipes = {}
with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        pid, pipes = map(lambda s: s.strip(), line.split('<->'))
        pid = int(pid)
        pipes = list(map(int, map(lambda s: s.strip(), pipes.split(', '))))
        pid_pipes[pid] = pipes

def add_to_group(pid, visited, in_group):
    if pid in visited:
        return visited, in_group
    in_group += pid_pipes[pid]
    visited.append(pid)
    for ppid in pid_pipes[pid]:
        visited, in_group = add_to_group(ppid, visited, in_group)
    return visited, in_group

visited, in_group = add_to_group(0, [], [])

groups = {0: in_group}
for pid in pid_pipes.keys():
    if pid not in visited:
        visited, in_group = add_to_group(pid, visited, [])
        groups[pid] = in_group

print (len(groups.keys()))

