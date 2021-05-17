import copy

graph = [
    (1, 2, 5),
    (1, 3, 0),
    (2, 3, -7),
    (3, 4, 35),
]


def extract_graph_node():
    nodes = set()
    for i in graph:
        src, dest, weight = i
        nodes.add(src)
        nodes.add(dest)
    return nodes


def build_cost_parents(start):
    cost_parents = dict()
    for k, v in enumerate(graph):
        src, dest, weight = v
        cost_parents[dest] = float('inf'), None
    cost_parents[start] = 0, None
    return cost_parents


def bellman_ford():
    for i in range(graph_node_count - 1):
        copy_cost_parents = copy.deepcopy(cost_parents)
        for t in range(graph_node_count):
            src, dest, weight = graph[t]
            if copy_cost_parents[dest][0] > copy_cost_parents[src][0] + weight \
                    and copy_cost_parents[src][0] is not float('inf'):
                cost_parents[dest] = copy_cost_parents[src][0] + weight, src


if __name__ == "__main__":
    graph_route_count = len(graph)
    graph_node_count = len(extract_graph_node())
    cost_parents = build_cost_parents(1)
    bellman_ford()
    print(cost_parents)
