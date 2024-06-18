import unittest
import index 

S = index 
bubbleSort = S.bubblesort
# selectionSort = S.selectionSort
# mergeSort = S.mergeSort

class Test(unittest.TestCase):
    def getArray(self):
        return [100, -40, 500, -124, 0, 21, 7]

    def getSortedArray(self):
        return [-124, -40, 0, 7, 21, 100, 500]

    def test_bubble_sort(self):
        self.assertEqual(bubbleSort(self.getArray()), self.getSortedArray())


if __name__=='__main__':
    unittest.main()