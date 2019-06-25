"""

    Author: Abas Farah

    This is a unitest file for countingSort.py


"""

import unittest
from Algo_DS_Python.algorithms.sorting.countingSort import countingSort

class TestCountingSort(unittest.TestCase):
    def sort(self, lst):
        copy = lst[:]
        countingSort(lst, 100)
        return lst

    def test_CountingSort(self):
        lst = [1,4,5,6,8,99,2,3]
        sorted_lst = self.sort(lst)
        # test countingSort on list types
        self.assertEqual(sorted_lst, lst)

    def test_EmptyList(self):
        lst = []
        self.assertEqual(self.sort(lst), [])

if __name__=='__main__':
    unittest.main()
