'''
Depth first search.
Time Complexity O(V+E)
Space Complexity O(V)

Traverse nodes and neighbor nodes. Don't visit more than once. Also can handle disconnected graphs.
'''


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)



    def addEdge(self, u, v):
        self.graph[u].append(v)



    def DFSUtil(self, v, visited):
        #Mark the current node as visited and print it.
        visited.add(v)
        print(v)



        #Recursively visit adjacent nodes.
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)



    def DFS(self):
        #Create a set to store all visited vertices
        visited=set()
        #call the recursive helper
        for vertex in self.graph:
            for vertex in self.graph:
                if vertex not in visited:
                    self.DFSUtil(vertex, visited)



graph = Graph()
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,2)
graph.addEdge(2,0)
graph.addEdge(2,3)
graph.addEdge(3,3)
graph.addEdge(9,9)
graph.DFS()
