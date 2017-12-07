#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as input_file:
    line = input_file.readline()

initial_state = [int(block) for block in line.split()]
num_banks = len(initial_state)
states = [' '.join([str(block) for block in initial_state])]

count = 0
current_state = initial_state
while True:
    count += 1

    old_state = current_state
    largest_bank_pos = 0
    largest_bank_val = 0
    for i in range(num_banks):
        if old_state[i] > largest_bank_val:
            largest_bank_pos = i
            largest_bank_val = old_state[i]
    current_state[largest_bank_pos] = 0
    div_banks = largest_bank_val // num_banks
    mod_banks = largest_bank_val % num_banks
    for i in range(num_banks):
        current_state[i] += div_banks
    for i in range(mod_banks):
        address = (largest_bank_pos + i + 1) % num_banks
        current_state[address] += 1

    bank_string = ' '.join([str(block) for block in current_state])
    if bank_string in states:
        break
    else:
        states.append(bank_string)

start_pos = states.index(bank_string)
duration = count - start_pos
print (duration)
