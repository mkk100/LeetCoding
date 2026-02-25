import collections


def dfs(graph, root):  # for graph
    stack = [root]
    while stack:
        node = stack.pop()
        print(node)
        for n in graph[node]:
            stack.append(n)


def dfsRecur(graph, root, visited=None):
    if visited is None:
        visited = set()
    visited.add(root)
    print(root)
    
    for i in graph[root]:
        if i not in visited:
            dfsRecur(graph, i, visited)

def dfs(graph, root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node)
        for n in graph[node]:
            stack.append(n) 

def dfs_recursive(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    print(start_node, end=" ")  # Process the current node (e.g., print it)

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def bfs(graph, root):  # adjacency list
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        print(node)
        for n in graph[node]:
            queue.append(n)


def bfs(graph, root):
    queue = []
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node)
        for i in range(graph[node]):
            queue.append(n)

def bfs_adjacency_matrix(graph, root):
    queue = []
    queue.append(root)
    visited = [False] * len(graph)
    visited[root] = True
    
    while queue:
        node = queue.popleft()
        for i in range(graph[node]):
            if graph[node][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True
    return queue
            

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

def bfsPractice(graph, root):
    queue = collections.deque([root])
    while queue:
        queueNode = queue.popleft()
        print(queueNode)
        for i in graph[queueNode]:
            if i not in queue:
                queue.append(i)
            
def bfsAdjMatrix(adj_matrix, root):
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

def bellmanFord(graph, v, src):
    dist = [inf] * v
    dist[src] = 0
    
    for n in range(v - 1):
        for u,v,w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    affected = [false] * v
    for _ in range(v):
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                print("Negative cycle detected")
                dist[v] = -inf
                affected[v] = True
        if affected[u]:
            affected[v] = True
            dist[v] = -inf
            
    return dist

def bellmanFord(graph, v, src):
    dist = [inf] * v
    dist[src] = 0
    for _ in range(v):
        for u,w in range(v):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for _ in range(v):
        for u,w in range(v):
            if dist[u] + w < dist[v]:
                print("Negative cycle")
            

def dijkstra(graph,root):
    heap = [float("inf")] * len(graph)
    heap[root] = (0,root)  
    
    while heap:
        node, u = heap.pop()
        for v, w in graph[node]:
            if heap[u] + w < heap[v]:
                heap[v] = heap[u] + w
                heap.push(heap[v], w)
         
        
def topSort(graph): # bfs based
    # Initialize in-degree for all nodes
    # count in-degrees
    in_degree = collections.defaultdict(int)
    # count in-degrees
    
    # Add all nodes with 0 in-degree to the queue
    queue = []
    # res will store final topological order
    result = []
    while queue:
        node = queue.popleft()
        for i in graph[node]: # for each node it points, reduce their in-degree
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)
    
    if len(result) != len(graph):
        print("Graph has a cycle")
            
    return result

def topSort(graph):
    in_deg = []
    # count the in_deg to the node
    queue = []
    result = []
    while queue:
        node = queue.popleft()
        for i in range(graph[node]):
            in_deg[i] -= 1
            if in_deg[i] == 0:
                queue.append(i)
    return res


def transitiveClosure(graph): # bfs based
    for v in graph: # for every vertex
        queue = deque()
        queue.append(v)
        visited = set()
        visited.add(v)
        # Bfs
        while queue:
            w = queue.popleft()
            
            for w1 in graph[w]:
                # if the edge doesn't exist
                if w1 not in graph[v]:
                    queue.append(w1) # then add
                
                if w1 not in visited:
                    visited.add(w1)
                    queue.append(w1)
    return graph

# accounting and masters
# dynamic programming & greedy structures
# overview of the algorithms again
# Algo analysis and proofs left
    
     

graph = {
    "A": ["C", "B"],
         "B": ["D"],
         "C": ["E"],
         "D": ["F"],
         "E": [],
         "F": []
    }

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
print("BFS Practice")
bfsPractice(graph, "A")
print("BFS Adjacency Matrix")
bfs_adjacencyMatrix(adj_matrix, 0)
