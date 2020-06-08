from collections import defaultdict
from json import dumps

def depth_first_search(graph, starting_vertex):
    visited = set()
    counter = [0]
    traversal_times = defaultdict(dict)

    def traverse(vertex):
        visited.add(vertex)
        counter[0] += 1
        traversal_times[vertex]['discovery'] = counter[0]

        for next_vertex in graph[vertex]:
            if next_vertex not in visited:
                traverse(next_vertex)

        counter[0] += 1
        traversal_times[vertex]['finish'] = counter[0]

    def connected_component():
        for vertex in graph:
            if vertex not in visited:
                print(f'vertex not visited: {vertex}')

    traverse(starting_vertex)
    connected_component()
    return traversal_times

def check_is_strong_connected_component(graph, start):
    reversed_graph = defaultdict(list)
    for vertex, edges in graph.items():
        for edge in edges:
            reversed_graph[edge].append(vertex)
    depth_first_search(reversed_graph, start)

graph={
  'a': ['b', 'd'],
  'b': ['c', 'd'],
  'c': ['e'],
  'd': ['e'],
  'e': ['b', 'f', 'g'],
  'f': ['c', 'h', 'i'],
  'g': ['d', 'h'],
  'h': ['e', 'i'],
  'i': []
}

start = 'a'
traversal_times = depth_first_search(graph, start)
print(dumps(traversal_times, indent = 4))
check_is_strong_connected_component(graph, start)