from aoc import *


def calculate_fuel(input_number):
    return input_number // 3 - 2


def first_part(input_numbers):
    result = 0
    for i in input_numbers:
        result += calculate_fuel(i)
    return result


def second_part(input_numbers):
    result = 0
    total = 0
    for i in input_numbers:
        result += calculate_fuel(i)
        total = calculate_fuel(i)
        while calculate_fuel(total) > 0:
            total = calculate_fuel(total)
            result += total
    return result

input_list = read_input("Inputs\\Day1.txt")
input_numbers = list(map(int, input_list))

print(first_part(input_numbers))
print(second_part(input_numbers))