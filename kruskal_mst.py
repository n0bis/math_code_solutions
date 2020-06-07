from contextlib import suppress
from operator import itemgetter


def kruskal(graph, print_result = False):
    graph = sorted(graph, key=itemgetter(1))  # Sort the connections by value
    tree = []

    for connection in graph:  # Iterate through available connections
        if not creates_circuit(tree, connection, graph):
            tree.append(connection)  # Add the connection to our tree IF no circuits would be created

    if print_result:
        print_tree(tree)

    return tree


# Returns a list of all the nodes in the graph or tree
def get_nodes(graph) -> list:
    return sorted(set((i for x in graph for i in x[0])))


# Returns a boolean of whether adding the specified connection to the tree would create a circuit.
def creates_circuit(tree, conn, graph) -> bool:
    tree = list(tree)
    if len(tree) == 0:
        return False  # Adding a connection can't create a circuit if the tree is empty
    tree.append(conn)

    nodes = get_nodes(tree)
    max_steps = len(graph) - 1

    # Returns a list of points connected to a given point
    def connected_to(point, exclude):
        result = list(
            map(lambda y: y.replace(point, ""),  # Get the other point in the connections
                filter(lambda x: point in x,  # Filter out connections that don't touch the point in question
                       map(itemgetter(0), tree)  # Get the points in the connection
                       )
                ))

        if exclude in result:
            result.remove(exclude)

        return result

    # Returns whether the current path successfully terminates
    def move(prev, curr, steps):
        steps += 1
        with suppress(ValueError):
            nodes.remove(curr)
        # If the number of "steps" is more than the possible connections of the tree, then it must be looping.
        if steps > max_steps:
            return False
        paths = connected_to(curr, prev)
        paths_terminate = [move(curr, path, steps) for path in paths]
        return False not in paths_terminate

    # The tree may have "broken branches", where two or more parts are disconnected.
    # We therefore make sure that all the nodes in our tree are checked over.
    while len(nodes) > 0:
        if not move(None, nodes[0], -1):
            return True
    return False


# Prints a tree and its length
def print_tree(tree):
    for conn, val in tree:
        print("{}: {}".format(conn, val))

    total = sum(map(itemgetter(1), tree))
    print("\nTree total: {}".format(total))

graph = [
	("AE", 8),
    ("AB", 17),
    ("AF", 10),
    ("EH", -4),
    ("ED", 6),
    ("FH", -10),
    ("FG", 25),
    ("BG", -5),
    ("BC", 19),
    ("HD", 1),
    ("HG", -12),
    ("GC", -3),
    ("DC", 2)
]

print(kruskal(graph, print_result=True))