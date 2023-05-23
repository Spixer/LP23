from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        visited = [False] * len(self.graph)
        self._dfs(start, visited)

    def _dfs(self, u, visited):
        visited[u] = True
        print(u, end=" ")

        for v in self.graph[u]:
            if not visited[v]:
                self._dfs(v, visited)

    def bfs(self, start):
        visited = [False] * len(self.graph)
        queue = []

        visited[start] = True
        queue.append(start)

        while queue:
            u = queue.pop(0)
            print(u, end=" ")

            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)


# User input for graph
g = Graph()
vertices = int(input("Enter the number of vertices: "))

for i in range(vertices):
    edges = input("Enter the edges for vertex " + str(i) + " (separated by space): ")
    edges_list = list(map(int, edges.split()))

    for j in range(1, len(edges_list)):
        g.add_edge(i, edges_list[j])

start_vertex = int(input("Enter the starting vertex: "))

choice = input("For DFS wirte DFS\n For BFS write BFS")
if choice == "DFS":
    print("DFS traversal:\n")
    g.dfs(start_vertex)
elif choice == "BFS":
    print("BFS traversal:\n")
    g.bfs(start_vertex)
else:
    print(" Invalid Choice\n")


"""

Enter the number of vertices: 6
Enter the edges for vertex 0 (separated by space): 0 1 2 3
Enter the edges for vertex 1 (separated by space): 1 0 4
Enter the edges for vertex 2 (separated by space): 2 0 5
Enter the edges for vertex 3 (separated by space): 3 0
Enter the edges for vertex 4 (separated by space): 4 1
Enter the edges for vertex 5 (separated by space): 5 2
Enter the starting vertex: 0
For DFS wirte DFS
 For BFS write BFSDFS
DFS traversal:

0 1 4 2 5 3 %                                                                          
(base) spider@Oms-MacBook-Air Practicals % /usr/local/bin/python3 /Users/spider/Desktop/Practicals/LP2-Assignments/AI/Assignment1/bfs-dfs.py
Enter the number of vertices: 6
Enter the edges for vertex 0 (separated by space): 0 1 2 3
Enter the edges for vertex 1 (separated by space): 1 0 4
Enter the edges for vertex 2 (separated by space): 2 0 5
Enter the edges for vertex 3 (separated by space): 3 0
Enter the edges for vertex 4 (separated by space): 4 1
Enter the edges for vertex 5 (separated by space): 5 2
Enter the starting vertex: 0
For DFS wirte DFS
 For BFS write BFSBFS
BFS traversal:

0 1 2 3 4 5 %                                                                          
"""
