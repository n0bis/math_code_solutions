from collections import defaultdict
from json import dumps

simple_graph = {
  'a': ['b'],
  'b': ['c', 'e'],
  'c': ['d', 'f'],
  'd': ['g'],
  'e': ['a', 'f'],
  'f': ['b', 'g', 'h'],
  'g': ['c', 'i'],
  'h': ['e', 'i'],
  'i': ['f', 'j'],
  'j': ['h']
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

traversal_times = depth_first_search(simple_graph, 'a')
print(dumps(traversal_times, indent = 4))