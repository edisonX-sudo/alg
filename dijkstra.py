graph = dict()
graph["start"] = dict()
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = dict()
graph["a"]["fin"] = 1
graph["b"] = dict()
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

proccessed = set()


def build_cost_parents(start, end):
    cost_parents = dict()
    for k in graph:
        cost_parents[k] = float('inf'), None
    cost_parents[end] = float('inf'), None
    cost_parents[start] = 0, None
    return cost_parents


def dijkstra(end):
    least_cost_node, least_cost = find_least_cost_node(end)
    while least_cost_node is not None:
        for next_node, to_next_node_pass_cost in graph[least_cost_node].items():
            cur_cost = least_cost + to_next_node_pass_cost
            if cost_parents[next_node][0] > cur_cost:
                cost_parents[next_node] = cur_cost, least_cost_node
        proccessed.add(least_cost_node)
        least_cost_node, least_cost = find_least_cost_node(end)


def find_least_cost_node(end):
    min = float("inf")
    node_name = None
    for node, value in cost_parents.items():
        cost, parent = value
        if min > cost and node not in proccessed and node is not end:
            min = cost
            node_name = node
    return node_name, min


if __name__ == '__main__':
    cost_parents = build_cost_parents("start", "fin")
    dijkstra("fin")
    print(cost_parents)
