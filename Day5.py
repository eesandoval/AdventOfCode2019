from aoc import *


opcodes = {1: '+', 2: '*', 99: "STOP", 3: "IN", 4: "OUT", 5: "JMPT", 6: "JMPF", 7: "<", 8: "=="}


def index_resolver(lst, pc, instruction, power_of_ten, increment = 1):
    if instruction > 99 and (int)(instruction / (10 ** power_of_ten)) % 10 == 1:
        return pc + increment
    else:
        return lst[pc + increment]


def first_part(input_numbers):
    lst = input_numbers.copy()
    pc = 0
    while pc < len(lst):
        instruction = lst[pc]
        opcode = opcodes[instruction % 100]
        if opcode == "STOP":
            break
        elif opcode == "IN":
            lst[index_resolver(lst, pc, instruction, 2)] = (int)(input("Enter Integer Value: "))
            pc += 2
        elif opcode == "OUT":
            print(lst[index_resolver(lst, pc, instruction, 2)])
            pc += 2
        else:
            val1 = lst[index_resolver(lst, pc, instruction, 2)]
            val2 = lst[index_resolver(lst, pc, instruction, 3, 2)]
            lst[lst[pc + 3]] = eval("{0} {1} {2}".format(val1, opcode, val2))
            pc += 4
    return lst


def second_part(input_numbers):
    lst = input_numbers.copy()
    pc = 0
    while pc < len(lst):
        instruction = lst[pc]
        opcode = opcodes[instruction % 100]
        if opcode == "STOP":
            break
        elif opcode == "IN":
            lst[index_resolver(lst, pc, instruction, 2)] = (int)(input("Enter Integer Value: "))
            pc += 2
        elif opcode == "OUT":
            print(lst[index_resolver(lst, pc, instruction, 2)])
            pc += 2
        elif opcode == "JMPT":
            val1 = lst[index_resolver(lst, pc, instruction, 2)]
            if val1 > 0:
                pc = lst[index_resolver(lst, pc, instruction, 3, 2)]
            else:
                pc += 3
        elif opcode == "JMPF":
            val1 = lst[index_resolver(lst, pc, instruction, 2)]
            if val1 == 0:
                pc = lst[index_resolver(lst, pc, instruction, 3, 2)]
            else:
                pc += 3
        elif opcode == "<":
            val1 = lst[index_resolver(lst, pc, instruction, 2)]
            val2 = lst[index_resolver(lst, pc, instruction, 3, 2)]
            if val1 < val2:
                lst[index_resolver(lst, pc, instruction, 4, 3)] = 1
            else:
                lst[index_resolver(lst, pc, instruction, 4, 3)] = 0
            pc += 4
        elif opcode == "==":
            val1 = lst[index_resolver(lst, pc, instruction, 2)]
            val2 = lst[index_resolver(lst, pc, instruction, 3, 2)]
            if val1 == val2:
                lst[index_resolver(lst, pc, instruction, 4, 3)] = 1
            else:
                lst[index_resolver(lst, pc, instruction, 4, 3)] = 0
            pc += 4
        else:
            val1 = lst[index_resolver(lst, pc, instruction, 2)]
            val2 = lst[index_resolver(lst, pc, instruction, 3, 2)]
            lst[lst[pc + 3]] = eval("{0} {1} {2}".format(val1, opcode, val2))
            pc += 4
    return lst


input_list = read_input("Inputs\\Day5.txt")[0].strip()
input_numbers = list(map(int, input_list.split(',')))
first_part(input_numbers) # Input 1
second_part(input_numbers) # Input 5