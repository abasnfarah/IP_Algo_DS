"""

    Author: Abas Farah

    This is a unitest file for insertionSort.py

    Want to test that it runs on any int imput.


"""

import unittest
from Algo_DS_Python.algorithms.sorting.insertionSort import insertionSort

class TestInsertionSort(unittest.TestCase):
    def sort(self, lst):
        copy = lst[:]
        insertionSort(lst)
        return lst

    def test_InsertionSort(self):
        lst = [1,4,5,6,8,99,2,3]
        sorted_lst = self.sort(lst)
        # test insertionSort on list types
        self.assertEqual(sorted_lst, lst)

    def test_EmptyList(self):
        lst = []
        self.assertEqual(self.sort(lst), [])

if __name__=='__main__':
    unittest.main()
