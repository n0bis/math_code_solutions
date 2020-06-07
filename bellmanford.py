def bellman_ford(graph, source):
    # Step 1: Prepare the distance and predecessor for each node
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than the current, store it
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."
 
    return distance, predecessor
    
if __name__ == '__main__':
    graph = {
        'a': {'e': 8, 'f':  10, 'b': 17},
        'e': {'h': -4},
        'f': {'g': 25},
        'b': {'g': -5},
        'h': {'d': 1, 'f': -10},
        'g': {'c': -3, 'h': -12},
        'd': {'e': 6},
        'c': {'d': 2, 'b': 19}
    }

    distance, predecessor = bellman_ford(graph, source='a')

    print(distance)