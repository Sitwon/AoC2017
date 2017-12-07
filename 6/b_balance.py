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
        #print (program.name)
        root = program
        break

def true_weight(program):
    #print (program.name)
    if not program.children_names:
        #print (program.weight)
        return program.weight
    #print (repr(program.children_names))
    sub_weights = {
        child_name: true_weight(programs[child_name])
        for child_name in program.children_names
    }
    #print(repr(sub_weights))
    #print(sum(sub_weights.values()))
    sub_weights_set = set(sub_weights.values())
    program.sub_weights = sub_weights
    if len(sub_weights_set) != 1:
        print (repr(sub_weights))
        for child_name in program.children_names:
            child = programs[child_name]
            print (child_name, child.weight, repr(getattr(child, 'sub_weights', {})))
        sys.exit()
    return sum(sub_weights.values()) + program.weight

true_weight(root)

