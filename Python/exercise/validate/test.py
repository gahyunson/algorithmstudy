import unittest
import node
import index  

Node = node.Node
validate = index.validate

class Test(unittest.TestCase):
    def test_valid_bst(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)

        self.assertEqual(validate(n), True)

    def test_invalid_bst(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)
        n.left.left.right = Node(999)

        self.assertEqual(validate(n), False)


if __name__ == '__main__':
    unittest.main()

