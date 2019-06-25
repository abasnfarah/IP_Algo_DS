"""

    Author: Abas Farah

    This is a unitest file for randomized_QuickSort.py

"""

import unittest
from Algo_DS_Python.algorithms.sorting.randomQuickSort import randomized_QuickSort

class testRandmomQuickSort(unittest.TestCase):

    def sort(self, lst):
        copy = lst[:]
        randomized_QuickSort(lst)
        return lst

    def test_RandomQuickSort(self):
        lst = [3,1,5,8,6,9,22,7,2]

        sorted_lst = self.sort(lst)

        self.assertEqual(sorted_lst, lst)

    def test_EmptyList(self):
        lst = []
        self.assertEqual(self.sort(lst), [])


if __name__=='__main__':
    unittest.main()

