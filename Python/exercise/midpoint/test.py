import unittest 
import index 
import linkedlist
Node = linkedlist.Node
LinkedList = linkedlist.LinkedList
midpoint = index.midpoint

class TestMidpoint(unittest.TestCase):
    def test_midpoint_is_function(self):
        self.assertTrue(callable(midpoint))

    def test_midpoint_odd_numbered_list_3_elements(self):
        l = LinkedList()
        l.insertLast('a')
        l.insertLast('b')
        l.insertLast('c')
        self.assertEqual(midpoint(l).data, 'b')

    def test_midpoint_odd_numbered_list_5_elements(self):
        l = LinkedList()
        l.insertLast('a')
        l.insertLast('b')
        l.insertLast('c')
        l.insertLast('d')
        l.insertLast('e')
        self.assertEqual(midpoint(l).data, 'c')

    def test_midpoint_even_numbered_list_2_elements(self):
        l = LinkedList()
        l.insertLast('a')
        l.insertLast('b')
        self.assertEqual(midpoint(l).data, 'a')

    def test_midpoint_even_numbered_list_4_elements(self):
        l = LinkedList()
        l.insertLast('a')
        l.insertLast('b')
        l.insertLast('c')
        l.insertLast('d')
        self.assertEqual(midpoint(l).data, 'b')

if __name__ == '__main__':
    unittest.main()