from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

if __name__ == '__main__':
    graph = Graph()

    for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
        graph.add_node(node)

    graph.add_edge('A', 'B', 6)
    graph.add_edge('B', 'E', 8)
    graph.add_edge('B', 'C', 9)
    graph.add_edge('C', 'F', 16)
    graph.add_edge('C', 'D', 2)
    graph.add_edge('D', 'G', 5)
    graph.add_edge('E', 'A', 13)
    graph.add_edge('E', 'F', 21)
    graph.add_edge('F', 'B', 11)
    graph.add_edge('F', 'G', 19)
    graph.add_edge('F', 'H', 15)
    graph.add_edge('G', 'C', 7)
    graph.add_edge('G', 'I', 4)
    graph.add_edge('H', 'E', 14)
    graph.add_edge('H', 'I', 17)
    graph.add_edge('I', 'F', 3)
    graph.add_edge('I', 'J', 12)
    graph.add_edge('J', 'H', 1)

    visited, path = dijkstra(graph, 'A')
    print(visited)
    print(path)