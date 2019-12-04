from collections import defaultdict 
from aoc import *


def manhattan_distance(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[0])


def get_wire_positions(wire):
    wire_positions = set()
    x, y = 0, 0
    for w in wire:
        for _ in range(0, int(w[1:])):
            if w[0] == 'R':
                x += 1
            elif w[0] == 'L':
                x -= 1
            elif w[0] == 'U':
                y += 1
            elif w[0] == 'D':
                y -= 1
            wire_positions.add((x, y))
    return wire_positions


def get_crossing_distances(wire, crossings):
    crossing = defaultdict(int)
    distance, x, y = 0, 0, 0
    for w in wire:
        for _ in range(0, int(w[1:])):
            if w[0] == 'R':
                x += 1
            elif w[0] == 'L':
                x -= 1
            elif w[0] == 'U':
                y += 1
            elif w[0] == 'D':
                y -= 1
            distance += 1
            
            if (x, y) in crossings:
                crossing[(x, y)] = distance
    return crossing
        


def first_part(wire1, wire2):
    wire1_positions = get_wire_positions(wire1)
    wire2_positions = get_wire_positions(wire2)
    crossings = wire1_positions.intersection(wire2_positions)
    return min(manhattan_distance(crossing, (0, 0)) for crossing in crossings)

def second_part(wire1, wire2):
    wire1_positions = get_wire_positions(wire1)
    wire2_positions = get_wire_positions(wire2)
    crossings = wire1_positions.intersection(wire2_positions)
    w1_crossing_distance = get_crossing_distances(wire1, crossings)
    w2_crossing_distance = get_crossing_distances(wire2, crossings)
    return min(w1_crossing_distance[crossing] + w2_crossing_distance[crossing] for crossing in crossings)


input_list = read_input("Inputs\\Day3.txt")
wire1 = input_list[0].split(',')
wire2 = input_list[1].split(',')
print(first_part(wire1, wire2))
print(second_part(wire1, wire2))