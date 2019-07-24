# John Shaw - jsha509 - 870608863
# Compsci220 - Assignment 4 - Question 2

import sys
from math import *

def shortestPath(numVertices,vertices,edges):
    queue = {}
    queue[0] = 0.0
    start = -1
    while(bool(queue)):
        min = float(numVertices)*100000000000000.00
        firstkey = -1
        for key in queue.keys():
            if(queue[key] <  min):
                min = queue[key]
                firstkey = key

        if(firstkey == numVertices-1):
            start = min
            break;
        # delete it from queue
        if (bool(queue)):
            del queue[firstkey]
        for v in edges[firstkey].keys():
            if (v not in queue):
                queue[v] = min + edges[firstkey][v]
            else:
                if(queue[v] > min + edges[firstkey][v]):
                    queue[v] = min + edges[firstkey][v]

    return(start)

for line in sys.stdin:
    data = line.split(',')
    size = len(data)
    n = data[0]
    vertices = {}
    numofvertices = 0
    for i in range(1,size):
        if(i%2 == 1):
            vertices[numofvertices] = ( float(data[i]) , float(data[i+1]) )
            numofvertices += 1
    edges = {}
    for u in vertices.keys():
        edges[u] = {}
        for v in vertices.keys():
            if( u != v):
                dist = (vertices[u][0]-vertices[v][0])*(vertices[u][0]-vertices[v][0]) + (vertices[u][1]-vertices[v][1])*(vertices[u][1]-vertices[v][1])
                if(dist <= 10000.0):
                    dist = sqrt(dist)
                    edges[u][v] = dist
    start = shortestPath(numofvertices,vertices,edges)
    if(start == -1):
        print(start)
    else:
        print('{0:.2f}'.format(start))
