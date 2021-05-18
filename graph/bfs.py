from collections import deque

graph = dict()
graph["you"] = ["alice", "bob", "claire"]

graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]

graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []

name_set = set()
squeue = deque()


def bfs(root, sword):
    add2squeue(root)
    while len(squeue) != 0:
        i = squeue.popleft()
        print(i)
        if i == sword:
            return True
        else:
            return bfs(graph[i], sword)
    return False


def add2squeue(root):
    for r in root:
        if r not in name_set:
            squeue.append(r)
            name_set.add(r)


if __name__ == '__main__':
    b = bfs(graph["you"], 'jonn')
    print(b)
