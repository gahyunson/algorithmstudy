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

    def test_insertLast(self):
        l = List()
        l.insertFirst('a')
        l.insertLast('b')
        self.assertEqual(l.size(), 2)
        self.assertEqual(l.getLast().data, 'b')

    def test_getAt(self):
        l = List()
        self.assertIsNone(l.getAt(10))

        l.insertLast(1)
        l.insertLast(2)
        l.insertLast(3)
        l.insertLast(4)

        self.assertEqual(l.getAt(0).data, 1)
        self.assertEqual(l.getAt(1).data, 2)
        self.assertEqual(l.getAt(2).data, 3)
        self.assertEqual(l.getAt(3).data, 4)

    # @unittest.skip("RemoveAt tests skipped")
    def test_removeAt(self):
        l = List()
        # with self.assertRaises():
        #     l.removeAt(0)
        #     l.removeAt(1)
        #     l.removeAt(2)
        self.assertIsNone(l.removeAt(0))
        self.assertIsNone(l.removeAt(1))
        self.assertIsNone(l.removeAt(2))

        l = List()
        l.insertFirst('a')
        l.removeAt(1)
        self.assertIsNone(l.removeAt(1))

        l = List()
        l.insertLast(1)
        l.insertLast(2)
        l.insertLast(3)
        l.insertLast(4)
        self.assertEqual(l.getAt(0).data, 1)
        l.removeAt(0)
        self.assertEqual(l.getAt(0).data, 2)

        l = List()
        l.insertLast(1)
        l.insertLast(2)
        l.insertLast(3)
        l.insertLast(4)
        self.assertEqual(l.getAt(1).data, 2)
        l.removeAt(1)
        self.assertEqual(l.getAt(1).data, 3)

        l = List()
        l.insertLast(1)
        l.insertLast(2)
        l.insertLast(3)
        l.insertLast(4)
        self.assertEqual(l.getAt(3).data, 4)
        l.removeAt(3)
        self.assertIsNone(l.getAt(3), None)

    # @unittest.skip("InsertAt tests skipped")
    def test_insertAt(self):
        l = List()
        l.insertAt('hi', 0)
        self.assertEqual(l.getFirst().data, 'hi')

        l = List()
        l.insertLast('a')
        l.insertLast('b')
        l.insertLast('c')
        l.insertAt('hi', 0)
        self.assertEqual(l.getAt(0).data, 'hi')
        self.assertEqual(l.getAt(1).data, 'a')
        self.assertEqual(l.getAt(2).data, 'b')
        self.assertEqual(l.getAt(3).data, 'c')

        l = List()
        l.insertLast('a')
        l.insertLast('b')
        l.insertLast('c')
        l.insertLast('d')
        l.insertAt('hi', 2)
        self.assertEqual(l.getAt(0).data, 'a')
        self.assertEqual(l.getAt(1).data, 'b')
        self.assertEqual(l.getAt(2).data, 'hi')
        self.assertEqual(l.getAt(3).data, 'c')
        self.assertEqual(l.getAt(4).data, 'd')

        l = List()
        l.insertLast('a')
        l.insertLast('b')
        l.insertAt('hi', 2)
        self.assertEqual(l.getAt(0).data, 'a')
        self.assertEqual(l.getAt(1).data, 'b')
        self.assertEqual(l.getAt(2).data, 'hi')

        l = List()
        l.insertLast('a')
        l.insertLast('b')
        l.insertAt('hi', 30)
        self.assertEqual(l.getAt(0).data, 'a')
        self.assertEqual(l.getAt(1).data, 'b')
        self.assertEqual(l.getAt(2).data, 'hi')

    @unittest.skip("ForEach tests skipped")
    def test_forEach(self):
        l = List()

        l.insertLast(1)
        l.insertLast(2)
        l.insertLast(3)
        l.insertLast(4)

        l.forEach(lambda node: node.data + 10)

        self.assertEqual(l.getAt(0).data, 11)
        self.assertEqual(l.getAt(1).data, 12)
        self.assertEqual(l.getAt(2).data, 13)
        self.assertEqual(l.getAt(3).data, 14)

    @unittest.skip("for...of loops tests skipped")
    def test_for_of_loops(self):
        l = List()

        l.insertLast(1)
        l.insertLast(2)
        l.insertLast(3)
        l.insertLast(4)

        for node in l:
            node.data += 10

        self.assertEqual(l.getAt(0).data, 11)
        self.assertEqual(l.getAt(1).data, 12)
        self.assertEqual(l.getAt(2).data, 13)
        self.assertEqual(l.getAt(3).data, 14)

        l = List()
        self.assertIsNone(next(iter(l), None))

        


if __name__ == '__main__':
    unittest.main()