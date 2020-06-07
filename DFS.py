from collections import defaultdict
from json import dumps

simple_graph = {
  'a': ['i'],
  'b': ['a', 'c'],
  'c': ['i'],
  'd': ['c'],
  'e': ['d', 'i'],
  'f': ['e', 'i'],
  'g': ['f', 'h'],
  'h': ['a'],
  'i': ['b', 'd', 'g', 'h']
}


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

    traverse(starting_vertex)
    return traversal_times

start = 'i'
traversal_times = depth_first_search(simple_graph, start)
print(dumps(traversal_times, indent = 4))