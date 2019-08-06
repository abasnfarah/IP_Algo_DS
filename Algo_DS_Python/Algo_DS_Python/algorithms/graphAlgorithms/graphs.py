"""
    Author: Abas Farah

    This is code for graphs.py

    This file has some prebuilt graphs using the:
        --> Adjecency List
        --> Adjecency Matrix
        --> Adjecency List with edge weights
        --> Object oriented graph with edge weights

"""

import sys
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append('.')
sys.path.append(dirpath + '/../../data_structures/linkedList/')


# A Undirected graph with 7 nodes and edge weigths
# if nodes aren't connected it has a None value
adjecencyMatrix = [[None,    5,    7,    3, None, None, None, None],
                   [   5, None, None, None,    2,   10, None, None],
                   [   7, None, None, None, None, None,    1, None],
                   [   3, None, None, None, None, None, None,   11],
                   [None,    2, None, None, None, None, None,    9],
                   [None,   10, None, None, None, None, None,    4],
                   [None, None,    1, None, None, None, None,    6],
                   [None, None, None,   11,    9,    4,    6, None]]

# generating adjecencyList to match adjecency Matrix
def genAdjecencyList():
    adjecencyList = [None]*8
    for i in range(0,8):
        adjecencyList[i] = []

    for i in range(0,8):
        for j in range(0,8):
            if adjecencyMatrix[i][j] != None:
                adjecencyList[i].append(j)
    return adjecencyList

adjecencyList = genAdjecencyList()

dag = {'A':['C'],
       'B':['C','E'],
       'C':['D'],
       'E':['F'],
       'D':['F'],
       'F':['G'],
       'G':[]}













