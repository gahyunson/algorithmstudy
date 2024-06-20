import unittest
import index 

S = index 
bubbleSort = S.bubblesort
selectionSort = S.selectionSort
mergeSort = S.mergeSort
merge = S.merge 

class Test(unittest.TestCase):
    def getArray(self):
        return [100, -40, 500, -124, 0, 21, 7]

    def getSortedArray(self):
        return [-124, -40, 0, 7, 21, 100, 500]

    def test_bubble_sort(self):
        self.assertEqual(bubbleSort(self.getArray()), self.getSortedArray())

    def test_selection_sort(self):
        self.assertEqual(selectionSort(self.getArray()), self.getSortedArray())

    def test_merge_sort(self):
        left = [1, 10]
        right = [2, 8, 12]
        self.assertEqual(merge(left, right), [1,2,8,10,12])

    def test_mergesort(self):
        self.assertEqual(mergeSort(self.getArray()), self.getSortedArray())


if __name__=='__main__':
    unittest.main()