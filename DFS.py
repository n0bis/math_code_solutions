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

    traverse(starting_vertex)
    return traversal_times

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
print(dumps(sorted(traversal_times.items()), indent = 4))