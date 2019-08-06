"""
    Author: Abas Farah

    This is code for breadthFirstSearch Method on a graph (AdjecencyMatrix)
    Code can be easily adaptable on other graph implementations

    Runtime for BreadthFirstSearch:
        O(E) running time
        O(V + E) to list unreachable values from v (starting vertex)
"""

import sys
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append('.')
sys.path.append(dirpath + '/../../')

from graphs import adjecencyList as Adj
from data_structures.queue.queue import ArrayQueue


# This Function takes in a Adj being an adjecencyList and s being a starting Node
# This implementation is based off of CLRS.22.2 BreadthFirstSearch
def BFS(Adj, s):
    level = {s:0}
    parent = {s:None}
    i = 1
    frontier = [s]
    while frontier:
        nextLevel = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    nextLevel.append(v)

        frontier = nextLevel
        i += 1

    print(level)







