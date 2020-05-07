# cook your code here
"""After completion of the 3rd round I came to know that codes will shared with recuiter.
For that scanerio I want to say that I don't know python I write my codes in C++ so if there
are some cases where some better operation of pythons are used please consider it as new 
bee's mistake in python."""

#Reference https://www.youtube.com/watch?v=GiN3jRdgxU4&t=26s

# Max flow with multiple source and sink ford fulkerson algorithm
from Queue import Queue

def modify_graph(entrances, exits, path):
    """ Modify the graph to solve to solve mutlti source multi sink max flow problem"""

    new_adjacency_matrix=[[0 for i in range(len(path)+2)] for j in range(len(path)+2)]

    for i in entrances:
        new_adjacency_matrix[0][i+1]=float('inf')

    for i in exits:
        new_adjacency_matrix[i+1][len(path)+1]=float('inf')

    for i in range(len(path)):
        for j in range(len(path)):
            new_adjacency_matrix[i+1][j+1]=path[i][j]

    return new_adjacency_matrix

def solution(entrances, exits, path):
    
    path=modify_graph(entrances, exits, path)
    exits=[len(path)-1]
    entrances=[0]
       
    residual=path
    maxflow=0
    currentflow=-1

    while True:
        
        currentflow=float('inf')
        queue = Queue()
        queue.put(0)
        parent={}
        visited=[0]*len(path)
        visited[0]=1

        found_path=False
        
        #bfs to search for agumented path
        while not queue.empty():
            u= queue.get()
            for v in range(len(residual)):
                
                if visited[v]==0 and residual[u][v] > 0:    
                    parent[v]=u
                    visited[v]=1
                    queue.put(v)
                    if v==len(residual)-1:
                        found_path=True

        if not found_path:
            break
        
        v=len(residual)-1
        while v!=0:     #finding bottle neck flow
            u=parent[v]
            if currentflow>residual[u][v]:
                currentflow=residual[u][v]
            v=u
        
        maxflow+=currentflow

        v=len(residual)-1
        while v!=0:     #updating the residual matrix
            u=parent[v]
            residual[u][v]-=currentflow
            residual[v][u]+=currentflow
            v=u
        
    return maxflow