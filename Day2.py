from aoc import *


opcodes = {1: '+', 2: '*', 99: "STOP"}


def first_part(input_numbers):
    lst = input_numbers.copy()
    for i in range(0, len(lst), 4):
        opcode = opcodes[lst[i]]
        if opcode == "STOP":
            break
        val1 = lst[lst[i + 1]]
        val2 = lst[lst[i + 2]]
        lst[lst[i + 3]] = eval("{0} {1} {2}".format(val1, opcode, val2))
    return lst[0]


def second_part(input_numbers, expected_output):
    lst = input_numbers.copy()
    for noun in range(0, 99):
        lst[1] = noun
        for verb in range(0, 99):
            lst[2] = verb
            if first_part(lst) == expected_output:
                return 100 * noun + verb 
    return -1


input_list = read_input("Inputs\\Day2.txt")[0].strip()
input_numbers = list(map(int, input_list.split(',')))
print(first_part(input_numbers))
print(second_part(input_numbers, 19690720))