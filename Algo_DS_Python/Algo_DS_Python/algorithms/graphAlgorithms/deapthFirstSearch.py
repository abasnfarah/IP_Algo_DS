"""
    Author: Abas Farah

    This is code for depthFirstSearch Method on a graph (AdjecencyMatrix)
    Code can be easily adaptable on other graph implementations

    Runtime for DepthFirstSearch:
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
from data_structures.stacks.stacks import ArrayStack

parent = {0:None}

def DFS_Visit_Recursive(s, Adj):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_Visit_Recursive(v,Adj)


def DFS(V,Adj):
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_Visit_Recursive(s,Adj)

DFS(Adj[0],Adj)

