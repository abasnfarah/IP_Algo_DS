"""
    Author: Abas Farah

    This is code for TopologicalSort

    Topological sort takes a DAG(Directed Acyclic Graph) and
    performs a sort to list out in order the order in which nodes
    of the graph are dependent on previous nodes.

    if T is the set of all topological ordered sets for the DAG G
    then our function just returns 1 element from the set of T.

    Applications:
        Package Building considering dependencies.
        Scheduling
"""

import sys
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append('.')
sys.path.append(dirpath + '/../../data_structures/')

from graphs import dag as G
from stacks.stacks import ListStack as stack


def topologicalSort(graph):
    sortedStack = stack()
    visitedSet = {}

    # traverses every node till it's al looked at
    for vertex in graph:

        # If vertex isn't visited then will go ahead and traverse till all children are visited
        if(vertex not in visitedSet):
            topologicalSortUtil(vertex, graph, sortedStack, visitedSet)

    return sortedStack

def topologicalSortUtil(vertex, graph, sortedStack, visitedSet):
    # Add node to visited Set
    visitedSet[vertex] = vertex

    # Traversing graph using a DepthFirst strategy
    # will traverse children till leaf node is found
    # Once a node has all it's children visited recursivly
    # Then will ad to sorted stack
    for child in graph[vertex]:

        if child not in visitedSet:
            topologicalSortUtil(child, graph, sortedStack, visitedSet)
    sortedStack.push(vertex)









