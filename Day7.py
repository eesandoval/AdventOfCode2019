from aoc import *
from itertools import permutations


class Intcode():

    def __init__(self, input_numbers):
        self.input_numbers = input_numbers.copy()
        self.backup_numbers = input_numbers.copy()
        self.pc = 0
        self.stopped = False
        self.need_input = False
        self.need_input = True
        self.memory = []
        self.memory_i = 0
        self.opcodes = {1: '+', 2: '*', 99: "STOP", 3: "IN", 4: "OUT", 5: "JMPT", 6: "JMPF", 7: "<", 8: "=="}
    
    def reset(self):
        self.input_numbers = self.backup_numbers.copy()
        self.pc = 0
        self.stopped = False
        self.memory = []
        self.memory_i = 0

    def computer(self):
        while self.pc < len(self.input_numbers):
            instruction = self.input_numbers[self.pc]
            opcode = self.opcodes[instruction % 100]
            if opcode == "STOP":
                self.stopped = True
                self.pc = len(self.input_numbers)
                return
            elif opcode == "IN":
                if self.memory_i >= len(self.memory):
                    return # need new values
                self.input_numbers[self.index_resolver(instruction, 2)] = self.memory[self.memory_i]
                self.memory_i += 1
                self.pc += 2
            elif opcode == "OUT":
                output = self.input_numbers[self.index_resolver(instruction, 2)]
                self.pc += 2
                return output
            elif opcode == "JMPT":
                val1 = self.input_numbers[self.index_resolver(instruction, 2)]
                if val1 > 0:
                    self.pc = self.input_numbers[self.index_resolver(instruction, 3, 2)]
                else:
                    self.pc += 3
            elif opcode == "JMPF":
                val1 = self.input_numbers[self.index_resolver(instruction, 2)]
                if val1 == 0:
                    self.pc = self.input_numbers[self.index_resolver(instruction, 3, 2)]
                else:
                    self.pc += 3
            elif opcode == "<":
                val1 = self.input_numbers[self.index_resolver(instruction, 2)]
                val2 = self.input_numbers[self.index_resolver(instruction, 3, 2)]
                if val1 < val2:
                    self.input_numbers[self.index_resolver(instruction, 4, 3)] = 1
                else:
                    self.input_numbers[self.index_resolver(instruction, 4, 3)] = 0
                self.pc += 4
            elif opcode == "==":
                val1 = self.input_numbers[self.index_resolver(instruction, 2)]
                val2 = self.input_numbers[self.index_resolver(instruction, 3, 2)]
                if val1 == val2:
                    self.input_numbers[self.index_resolver(instruction, 4, 3)] = 1
                else:
                    self.input_numbers[self.index_resolver(instruction, 4, 3)] = 0
                self.pc += 4
            else:
                val1 = self.input_numbers[self.index_resolver(instruction, 2)]
                val2 = self.input_numbers[self.index_resolver(instruction, 3, 2)]
                self.input_numbers[self.input_numbers[self.pc + 3]] = eval("{0} {1} {2}".format(val1, opcode, val2))
                self.pc += 4

    def index_resolver(self, instruction, power_of_ten, increment = 1):
        if instruction > 99 and (int)(instruction / (10 ** power_of_ten)) % 10 == 1:
            return self.pc + increment
        else:
            return self.input_numbers[self.pc + increment]


def get_intcode_value(phase, prev, input_numbers):
    intcode = Intcode(input_numbers)
    intcode.memory.append(phase)
    intcode.memory.append(prev)
    output = intcode.computer()
    return output


def first_part(input_numbers):
    max_value = 0
    possible_phases = list(permutations([1, 2, 3, 4, 0], 5))
    for phase in possible_phases:
        A_Out = get_intcode_value(phase[0], 0, input_numbers)
        B_Out = get_intcode_value(phase[1], A_Out, input_numbers)
        C_Out = get_intcode_value(phase[2], B_Out, input_numbers)
        D_Out = get_intcode_value(phase[3], C_Out, input_numbers)
        E_Out = get_intcode_value(phase[4], D_Out, input_numbers)
        max_value = max(max_value, E_Out)
    return max_value


def second_part(input_numbers):
    max_value = 0
    possible_phases = list(permutations([5, 6, 7, 8, 9], 5))
    intcodes = [Intcode(input_numbers), Intcode(input_numbers), Intcode(input_numbers), Intcode(input_numbers), Intcode(input_numbers)]
    for phase in possible_phases:
        for intcode in intcodes:
            intcode.reset()
        intcodes[0].memory.append(phase[0])
        intcodes[0].memory.append(0)
        intcodes[1].memory.append(phase[1])
        intcodes[2].memory.append(phase[2])
        intcodes[3].memory.append(phase[3])
        intcodes[4].memory.append(phase[4])
        last_E_Out = 0
        while not(intcodes[4].stopped):
            A_Out = intcodes[0].computer()
            if A_Out != None:
                intcodes[1].memory.append(A_Out)
            B_Out = intcodes[1].computer()
            if B_Out != None:
                intcodes[2].memory.append(B_Out)
            C_Out = intcodes[2].computer()
            if C_Out != None:
                intcodes[3].memory.append(C_Out)
            D_Out = intcodes[3].computer()
            if D_Out != None:
                intcodes[4].memory.append(D_Out)
            E_Out = intcodes[4].computer()
            if E_Out != None:
                intcodes[0].memory.append(E_Out)
                last_E_Out = E_Out
        max_value = max(max_value, last_E_Out)
    return max_value


input_list = read_input("Inputs\\Day7.txt")[0].strip()
input_numbers = list(map(int, input_list.split(',')))
print(first_part(input_numbers))
print(second_part(input_numbers))