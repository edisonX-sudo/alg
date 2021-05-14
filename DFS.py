from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]

graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]

graph["dick"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []

graph["peggy"] = ["dick"]

nameSet = {}
sQueue = deque()


def bfs(root, sword):
    global sQueue
    add2sQueu(root)
    while len(sQueue) != 0:
        i = sQueue.pop()
        print(i)
        if i == sword:
            return True
        else:
            return bfs(graph[i], sword)
    return False


def add2sQueu(root):
    for r in root:
        if not nameSet.has_key(r):
            sQueue.append(r)
            nameSet[r] = "set"


if __name__ == '__main__':
    b = bfs(graph["you"], 'jonn')
    print(b)
