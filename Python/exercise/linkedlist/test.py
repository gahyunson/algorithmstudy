import unittest 
import index

Node = index.Node
List = index.LinkedList


class Test(unittest.TestCase):

    def test_node(self):
        node = Node('a', 'b')
        self.assertEqual(node.data, 'a')
        self.assertEqual(node.next, 'b')

    def test_insertFirst(self):
        l = List()
        l.insertFirst(1)
        self.assertEqual(l.head.data, 1)
        l.insertFirst(2)
        self.assertEqual(l.head.data, 2)

if __name__ == '__main__':
    unittest.main()