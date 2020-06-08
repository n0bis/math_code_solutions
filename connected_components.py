from collections import defaultdict 

#This class represents a directed graph using adjacency list representation 
class Graph: 

    def __init__(self,graph): 
        self.graph = graph #defaultdict(list) # default dictionary to store graph

    # A function used by DFS 
    def DFSUtil(self,v,visited): 
        # Mark the current node as visited and print it 
        visited[v] = True
        print(v, end=' ')
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]:
            if visited[i]==False: 
                self.DFSUtil(i,visited) 

    def fillOrder(self,v,visited, stack): 
        # Mark the current node as visited  
        visited[v]= True
        
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]:
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
        stack = stack.append(v) 

    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
        g = Graph(self.graph)

        reversed_graph = defaultdict(list)
        for vertex, edges in self.graph.items():
            for edge in edges:
                reversed_graph[edge].append(vertex)
        
        return reversed_graph

    # The main function that finds and prints all strongly 
    # connected components 
    def printSCCs(self): 

        stack = [] 
        # Mark all the vertices as not visited (For first DFS) 
        visited = { vertex: False for vertex in graph.keys() }
        # Fill vertices in stack according to their finishing 
        # times
        for vertex in graph.keys():
            if visited[vertex]==False: 
                self.fillOrder(vertex, visited, stack) 

        # Create a reversed graph 
        reversed_graph = self.getTranspose() 
        gr = Graph(reversed_graph)
        
        # Mark all the vertices as not visited (For second DFS) 
        visited = { vertex: False for vertex in graph.keys() }
        # Now process all vertices in order defined by Stack 
        while stack: 
            i = stack.pop() 
            if visited[i]==False: 
                gr.DFSUtil(i, visited) 
                print('')

graph={
  'a': ['b', 'd'],
  'b': ['c', 'd'],
  'c': ['e'],
  'd': ['e'],
  'e': ['b', 'f', 'g'],
  'f': ['c', 'h', 'i'],
  'g': ['d', 'h'],
  'h': ['e', 'i'],
  'i': []
}

connected_component = Graph(graph)

print ("Following are strongly connected components in given graph") 
connected_component.printSCCs() 