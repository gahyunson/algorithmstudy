import unittest
import node 
import index 

Node = node.Node
levelwidth = index.levelWidth

class TestLevelWidth(unittest.TestCase):
    def test_levelwidth_is_function(self):
        self.assertTrue(callable(levelwidth))

    def test_levelwidth_returns_number_of_nodes_at_widest_point_1(self):
        root = Node(0)
        root.add(1)
        root.add(2)
        root.add(3)
        root.children[0].add(4)
        root.children[2].add(5)

        self.assertEqual(levelwidth(root), [1, 3, 2])

    def test_levelwidth_returns_number_of_nodes_at_widest_point_2(self):
        root = Node(0)
        root.add(1)
        root.children[0].add(2)
        root.children[0].add(3)
        root.children[0].children[0].add(4)

        self.assertEqual(levelwidth(root), [1, 1, 2, 1])

if __name__ == '__main__':
    unittest.main()