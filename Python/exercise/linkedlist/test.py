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
    
    def test_size(self):
        l = List()
        self.assertEqual(l.size(), 0)
        l.insertFirst(1)
        l.insertFirst(1)
        l.insertFirst(1)
        l.insertFirst(1)
        self.assertEqual(l.size(), 4)

    def test_getFirst(self):
        l = List()
        l.insertFirst(1)
        self.assertEqual(l.getFirst().data, 1)
        l.insertFirst(2)
        self.assertEqual(l.getFirst().data, 2)

    def test_getLast(self):
        l = List()
        l.insertFirst(2)
        self.assertEqual(l.getLast().data, 2)
        self.assertIsNone(l.getLast().next)
        l.insertFirst(1)
        self.assertEqual(l.getLast().data, 2)
        self.assertIsNone(l.getLast().next)

    def test_clear(self):
        l = List()
        self.assertEqual(l.size(), 0)
        l.insertFirst(1)
        l.insertFirst(1)
        l.insertFirst(1)
        l.insertFirst(1)
        self.assertEqual(l.size(), 4)
        l.clear()
        self.assertEqual(l.size(), 0)

    def test_removeFirst(self):
        # Test 'removes the first node when the list has a size of one'
        l = List()
        l.insertFirst('a')
        l.removeFirst()
        # Checking the size of the list after removal
        self.assertEqual(l.size(), 0)
        # Checking the first node after removal
        self.assertIsNone(l.getFirst())

    def test_removeLast(self):
        l = List()
        # This checks if removeLast does not raise an exception
        try:
            l.removeLast()
        except Exception as e:
            self.fail(f"removeLast() raised an exception {e}")

        l = List()
        l.insertFirst('a')
        l.removeLast()
        self.assertIsNone(l.head)

        l = List()
        l.insertFirst('b')
        l.insertFirst('a')
        l.removeLast()
        self.assertEqual(l.size(), 1)
        self.assertEqual(l.head.data, 'a')

        l = List()
        l.insertFirst('c')
        l.insertFirst('b')
        l.insertFirst('a')
        l.removeLast()
        self.assertEqual(l.size(), 2)
        self.assertEqual(l.getLast().data, 'b')

        


if __name__ == '__main__':
    unittest.main()