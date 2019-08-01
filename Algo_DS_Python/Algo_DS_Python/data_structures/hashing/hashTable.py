"""
    Author: Abas Farah

    This is code for the HashTableChaining class. And the HashTableOpenAddressing class:

    The Properties of the HashTableC (Chaining) Class:
        Atributes: hashTable (array of linkedLists)
        Methods: Insert, hash, delete, search

    The Properties of the HashTableOA (Open Addressing)
        Atributes: hashTable( array of hashed elements)
        Methods: Insert, hash, delete, search, tableDouble, tableReduce

"""

import sys
import os

# Using linkedList python Implementation
# Getting directory of script being run
# Then adding our linkedList implementation to our python Path
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append('.')
sys.path.append(dirpath + '/../linkedList')
from linkedList import LinkedList

# This is a class definition for a hash table using linkedList chaining
# to avoid colisions
# This implementation uses a fixed hash table length
# To see an implentation of a dynamic hash table look at HashTableOA
class HashTableC:
    def __init__(self, item=None):
        self.hashTable = [LinkedList()]* 31
        if (item != None):
            self.Insert(item)

    def printHF(self):
        for element in self.hashTable:
            print(element)
            print(" ")

    def hashFunction(self, key):
       # This returns a hash function mod 353 (prime)
       return key % 31

    # This takes an item generates a key then hashes that key to 
    # our hash table
    def insert(self, item):
        key = hash(item)

        index = self.hashFunction(key)

        self.hashTable[index].insertHead(item)

    def delete(self, item):
        key = hash(item)

        index = self.hashFunction(key)

        self.hashTable[index].deleteItem(item)

    def search(self, item):
        key = hash(item)
        index = self.hashFunction(key)

        return self.hashTable[index].find(item)

#x = HashTableC()
#x.insert(10)
#x.insert(5)
#x.insert(30)
#x.delete(5)
#x.printHF()
#
