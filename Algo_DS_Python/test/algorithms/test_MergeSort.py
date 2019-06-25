"""

    Author: Abas Farah

    This is a unitest file for mergeSort.py

"""

import unittest
from Algo_DS_Python.algorithms.sorting.mergeSort import mergeSort

class testMergeSort(unittest.TestCase):

    def sort(self, lst):
        copy = lst[:]
        mergeSort(lst)
        return lst

    def test_MergeSort(self):
        lst = [3,1,5,8,6,9,22,7,2]

        sorted_lst = self.sort(lst)

        self.assertEqual(sorted_lst, lst)

    def test_EmptyList(self):
        lst = []
        self.assertEqual(self.sort(lst), [])


if __name__=='__main__':
    unittest.main()
