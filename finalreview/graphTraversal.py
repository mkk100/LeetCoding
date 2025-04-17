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


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}

print("Iterative DFS")
dfs(graph, "A")
print("Recursive DFS")
dfsRecur(graph, "A")
