import collections


def dfs(graph, root):  # for graph
    stack = [root]
    while stack:
        node = stack.pop()
        print(node)
        for n in graph[node]:
            stack.append(n)


def dfsRecur(graph, root):
    print(root)
    for n in graph[root]:
        dfsRecur(graph, n)


def bfs(graph, root):  # adjacency list
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        print(node)
        for n in graph[node]:
            queue.append(n)


def bfs_adjacencyMatrix(adj_matrix, root):
    queue = collections.deque([root])
    visited = [False] * len(adj_matrix)
    visited[root] = True

    while queue:
        node = queue.popleft()
        print(node)
        for i in range(len(adj_matrix[node])):
            if adj_matrix[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)
    return queue


graph = {"A": ["C", "B"], "B": ["D"], "C": ["E"], "D": ["F"], "E": [], "F": []}

adj_matrix = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

print("Iterative DFS")
dfs(graph, "A")
print("Recursive DFS")
dfsRecur(graph, "A")
print("BFS")
bfs(graph, "A")
print("BFS Adjacency Matrix")
bfs_adjacencyMatrix(adj_matrix, 0)
