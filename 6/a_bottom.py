#!/usr/bin/env python3

import sys


class Program(object):
    def __init__(self, name, weight, children_names):
        self.name = name
        self.weight = weight
        self.children_names = children_names

programs = {}
with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        name = line.split(' ', 1)[0]
        weight = int(line.split(' ', 2)[1].strip('()\n'))
        children_names = None
        children_split = line.split(' -> ')
        if len(children_split) == 2:
            children_names = children_split[1].strip().split(', ')
        programs[name] = Program(name, weight, children_names)

possible_roots = list(filter(lambda p: p.children_names, programs.values()))

all_children = []
for program in possible_roots:
    all_children.extend(program.children_names)

for program in possible_roots:
    if program.name not in all_children:
        print (program.name)
        root = program
        break
