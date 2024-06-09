import unittest
from index import fromLast
import linkedlist
List = linkedlist.LinkedList
Node = linkedlist.Node

class Test(unittest.TestCase):
    def test_fromLast(self):
        l = List()

        l.insertLast('a')
        l.insertLast('b')
        l.insertLast('c')
        l.insertLast('d')
        l.insertLast('e')

        self.assertEqual(fromLast(l, 3).data, 'b')

if __name__ == '__main__':
    unittest.main()