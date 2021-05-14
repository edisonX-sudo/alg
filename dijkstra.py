graph = dict()
graph["start"] = dict()
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = dict()
graph["a"]["fin"] = 1
graph["b"] = dict()
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

proccessed = dict()


def build_costs(start, end):
    costs = dict()
    costs[end] = float('inf')
    for k in graph:
        if k is not start:
            costs[k] = float('inf')
    for k, v in graph[start].items():
        costs[k] = v
    return costs


def build_parents(start, end):
    parents = dict()
    parents[end] = None
    for k in graph:
        if k is not start:
            parents[k] = None
    for k in graph[start]:
        parents[k] = start
    return parents


def dijkstra(start, end):
    least_cost_node, least_cost = find_least_cost_node(end)
    while least_cost_node is not None:
        for next_node, to_next_node_pass_cost in graph[least_cost_node].items():
            cur_cost = least_cost + to_next_node_pass_cost
            if costs[next_node] > cur_cost:
                costs[next_node] = cur_cost
                parents[next_node] = least_cost_node
        proccessed[least_cost_node] = 'set'
        least_cost_node, least_cost = find_least_cost_node(end)
    return build_route(start, end), costs


def find_least_cost_node(end):
    min = float("inf")
    node_name = None
    for k, v in costs.items():
        if min > v and k not in proccessed and k is not end:
            min = v
            node_name = k
    return node_name, min


def build_route(start, end):
    p_inx = end
    route = [p_inx]
    while True:
        p_inx = parents[p_inx]
        route.append(p_inx)
        if p_inx is start:
            break
    return route


if __name__ == '__main__':
    costs = build_costs("start", "fin")
    parents = build_parents("start", "fin")
    print(dijkstra("start", "fin"))
