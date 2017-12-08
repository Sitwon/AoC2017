#!/usr/bin/env python3

import operator
import sys


registers = {}

conditions = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '!=': operator.ne,
    '==': operator.eq,
}

operations = {
    'inc': operator.add,
    'dec': operator.sub,
}

max_val = 0

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        register, op, value, _, cond_reg, cond, cond_val = line.split()
        # test condition
        LHS = registers.get(cond_reg, 0)
        RHS = int(cond_val)
        if not conditions[cond](LHS, RHS):
            continue
        # do the operaton
        if not register in registers.keys():
            registers[register] = 0
        registers[register] = operations[op](registers[register], int(value))
        current_max = max(registers.values())
        if current_max > max_val:
            max_val = current_max

print (max_val)
