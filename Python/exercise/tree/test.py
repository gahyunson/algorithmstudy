import unittest
from index import Node
from index import Tree

class TestNode(unittest.TestCase):
    def test_node_is_constructor(self):
        self.assertTrue(callable(Node))

    def test_node_has_data_and_children_properties(self):
        n = Node('a')
        self.assertEqual(n.data, 'a')
        self.assertEqual(len(n.children), 0)

    def test_node_can_add_children(self):
        n = Node('a')
        n.add('b')
        self.assertEqual(len(n.children), 1)
        self.assertEqual(len(n.children[0].children), 0)

    def test_node_can_remove_children(self):
        n = Node('a')
        n.add('b')
        self.assertEqual(len(n.children), 1)
        n.remove('b')
        self.assertEqual(len(n.children), 0)

# @unittest.skip("Tree tests skipped")
class TestTree(unittest.TestCase):
    def test_starts_empty(self):
        t = Tree()
        self.assertIsNone(t.root)

    def test_can_traverse_bf(self):
        letters = []
        t = Tree()
        t.root = Node('a')
        t.root.add('b')
        t.root.add('c')
        t.root.children[0].add('d')

        t.traverseBF(lambda node: letters.append(node.data))

        self.assertEqual(letters, ['a', 'b', 'c', 'd'])

    def test_can_traverse_df(self):
        letters = []
        t = Tree()
        t.root = Node('a')
        t.root.add('b')
        t.root.add('d')
        t.root.children[0].add('c')

        t.traverseDF(lambda node: letters.append(node.data))

        self.assertEqual(letters, ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
    unittest.main()