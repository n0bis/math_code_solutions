from collections import defaultdict
import heapq


def create_spanning_tree(graph, starting_vertex):
    mst = [] # defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            #print(frm, to)
            mst.append((frm, to))
            visited.add(to)
            #mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

example_graph = {
    'A': {'B': 4, 'H': 8, 'I': 7},
    'B': {'A': 4, 'C': 2, 'I': 6},
    'C': {'B': 2, 'D': 11, 'I': 22},
    'D': {'C': 11, 'E': 21, 'I': 18},
    'E': {'D': 21, 'F': 15, 'I': 14},
    'F': {'E': 15, 'G': 10, 'I': 5},
    'G': {'F': 10, 'H': 9, 'I': 13},
    'H': {'A': 8, 'G': 9, 'I': 17},
    'I': {'A': 7, 'B': 6, 'C': 22, 'D': 18, 'E': 14, 'F': 5, 'G': 13, 'H': 17}
}

print(create_spanning_tree(example_graph, 'A'))