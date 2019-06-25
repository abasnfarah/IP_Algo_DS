"""

    Author: Abas Farah

    This is a unittest file for radix_Sort.py

"""

import unittest
from Algo_DS_Python.algorithms.sorting.radixSort import radix_Sort

class testRadixSort(unittest.TestCase):

    def sort(self, lst, d):
        copy = lst[:]
        radix_Sort(lst, d)
        return lst

    def test_RadixSort(self):
        lst = [3,1,5,8,6,9,22,7,2]

        sorted_lst = self.sort(lst, 2)

        self.assertEqual(sorted_lst, lst)

    def test_EmptyList(self):
        lst = []
        self.assertEqual(self.sort(lst, 0), [])

    def test_HunderedsPlace(self):
        lst = [368,32,1,4,5,2,33,670,8,7,9]
        self.assertEqual(self.sort(lst, 3), [1, 2, 4, 5, 7, 8, 9, 32, 33, 368, 670])


if __name__=='__main__':
    unittest.main()
