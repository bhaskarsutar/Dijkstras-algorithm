#!/usr/bin/env python
# coding: utf-8

# # Dijkstra's algorithm
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# #### Dijkstras algorithm finds the shortest path between nodes in a network

# In the shortest path problem, we need to determine the shortest distance from a source to all other nodes or vertices in a
# graph. 
# 
# **Dijkstra's algorithm** is a very prominent method of solving this problem. This algorithm uses a greedy approach to solve the shortest path problem.
# It starts with the source node and finds the rest of the distances from the source node. Dijkstra’s algorithm keeps track of the currently known distance from the source node to the rest of the nodes and dynamically updates these values if a shorter path is found.
# 

# Consider the following graph:
# 
# <img src="https://s3-whjr-v2-prod-bucket.whjr.online/f1c63514-4715-4b5c-9f6b-9148448ca17c.PNG"/>

# #### Dijkstras algorithm :

# In[1]:


class Graph: 
    # A constructor to iniitialize the values
    def __init__(self, nodes):
        # distance array initialization
        self.distance_array = [0 for i in range(nodes)]
        #visited nodes initialization
        self.visited = [0 for i in range(nodes)]
        #initializing the number of nodes
        self.V = nodes
        #initializing the infinity value
        self.INF = 1000000
        #initializing the graph matrix
        self.graph = [[0 for column in range(nodes)]  
                    for row in range(nodes)]
   
    def dijkstra(self, srcNode):
        for i in range(self.V):
          #initialise the distances to infinity first
          self.distance_array[i] = self.INF
          #set the visited nodes set to false for each node
          self.visited[i] = False
        #initialise the first distance to 0
        self.distance_array[srcNode] = 0
        for i in range(self.V): 
  
            # Pick the minimum distance node from  
            # the set of nodes not yet processed.  
            # u is always equal to srcNode in first iteration 
            u = self.minDistance(self.distance_array, self.visited) 
  
            # Put the minimum distance node in the  
            # visited nodes set
            self.visited[u] = True
  
             # Update dist[v] only if is not in visited, there is an edge from 
            # u to v, and total weight of path from src to  v through u is 
            # smaller than current value of dist[v]
            for v in range(self.V): 
                if self.graph[u][v] > 0 and self.visited[v] == False and self.distance_array[v] > self.distance_array[u] + self.graph[u][v]: 
                        self.distance_array[v] = self.distance_array[u] + self.graph[u][v] 
  
        self.printSolution(self.distance_array, srcNode)

    #A utility function to find the node with minimum distance value, from 
    # the set of nodes not yet included in shortest path tree 
    def minDistance(self, distance_array, visited): 
  
        # Initilaize minimum distance for next node
        min = self.INF
  
        # Search not nearest node not in the  
        # unvisited nodes
        for v in range(self.V): 
            if distance_array[v] < min and visited[v] == False: 
                min = distance_array[v] 
                min_index = v 
  
        return min_index

    def printSolution(self, distance_array, srcNode): 
        print ("Node \tDistance from ", srcNode)
        for i in range(self.V): 
            print (i, "\t", distance_array[i])

# Display our table
ourGraph = Graph(7) 
ourGraph.graph = [[0, 2, 6, 0, 0, 0, 0], 
        [2, 0, 0, 5, 0, 0, 0], 
        [6, 6, 0, 8, 0, 0, 0], 
        [0, 0, 8, 0, 10, 15, 0], 
        [0, 0, 0, 10, 0, 6, 2], 
        [0, 0, 0, 15, 6, 0, 6], 
        [0, 0, 0, 0, 2, 6, 0],
        ]; 
  
ourGraph.dijkstra(0)

