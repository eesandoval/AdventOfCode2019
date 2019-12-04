from aoc import *


def first_part(range_min, range_max):
    result = []
    for i in range(range_min, range_max + 1):
        valid = False
        string = (str)(i)
        for sub_i in range(0, 5):
            if string[sub_i] == string[sub_i + 1]:
                valid = True
            if string[sub_i] > string[sub_i + 1]:
                valid = False
                break
        if valid:
            result.append(string)
    return result


def second_part(range_min, range_max):
    passwords = first_part(range_min, range_max)
    result = []
    for password in passwords:
        for c in password:
            if password.count(c) == 2:
                result.append(password)
                break 
    return result


range_string = read_input("Day4.txt")[0]
range_min = (int)(range_string.split('-')[0])
range_max = (int)(range_string.split('-')[1])
print(len(first_part(range_min, range_max)))
print(len(second_part(range_min, range_max)))