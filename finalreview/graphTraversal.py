def dfs(graph, root): # for graph
    stack = [root]
    while stack:
        node = stack.pop()
        print(node)
        for n in graph[node]:
            stack.append(n)


dfs({"A": ["B", "C"],
     "B": ["D", "E"],
     "C": ["F"],
     "D": [],
     "E": ["F"],
     "F": []}, "A")
