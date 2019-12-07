from aoc import *


class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def find_path(self, start_vertex, end_vertex, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None


def count_distance(node_dict, current_value):
    if node_dict[current_value] == "COM":
        return 1
    else:
        return 1 + count_distance(node_dict, node_dict[current_value])


def foo(node_dict, current_value):
    orbits = list(node_dict.values())
    if current_value not in orbits:
        return []
    lst = []
    for orbit in orbits:
        if orbit == current_value:
            lst.append(node_dict[orbit])
    return lst


def first_part(input_list):
    node_dict = {}
    for orbit in input_list:
        orbits = orbit.split(')')[0]
        value = orbit.split(')')[1].strip()
        node_dict[value] = orbits
    total = 0
    for value, orbits in node_dict.items():
        total += count_distance(node_dict, value)
    return total


def second_part(input_list):
    node_dict = {}
    for orbit in input_list:
        orbits = orbit.split(')')[0]
        value = orbit.split(')')[1].strip()
        if orbits in node_dict.keys():
            node_dict[orbits].append(value)
        else:
            node_dict[orbits] = [value]
        if value in node_dict.keys():
            node_dict[value].append(orbits)
        else:
            node_dict[value] = [orbits]
    graph = Graph(node_dict)
    path = graph.find_path("YOU", "SAN")
    return len(path) - 3


input_list = read_input("Inputs\\Day6.txt")
print(first_part(input_list)) # Input 1
print(second_part(input_list)) # Input 5