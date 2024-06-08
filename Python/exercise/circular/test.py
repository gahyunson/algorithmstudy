import unittest 
from index import circular 
import linkedlist

Node = linkedlist.Node
LinkedList = linkedlist.LinkedList

class TestCircular(unittest.TestCase):
    def test_circular_is_function(self):
        self.assertTrue(callable(circular))

    def test_circular_detects_circular_linked_lists(self):
        l = LinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')

        l.head = a
        a.next = b
        b.next = c
        c.next = b

        self.assertTrue(circular(l))

    def test_circular_detects_circular_linked_lists_linked_at_head(self):
        l = LinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')

        l.head = a
        a.next = b
        b.next = c
        c.next = a

        self.assertTrue(circular(l))

    def test_circular_detects_non_circular_linked_lists(self):
        l = LinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')

        l.head = a
        a.next = b
        b.next = c
        c.next = None

        self.assertFalse(circular(l))

if __name__ == '__main__':
    unittest.main()