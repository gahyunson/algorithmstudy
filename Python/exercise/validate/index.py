# --- Directions
# Given a node, validate the binary search tree,
# ensuring that every node's left hand child is
# less than the parent node's value, and that
# every node's right hand child is greater than
# the parent


def validate(node, min = None, max = None):
    # compare values
    if max != None and (node.data > max):
        return False
    if min != None and (node.data < min):
        return False
    
    # update max value if we move to node.left 
    if node.left and not validate(node.left, min = min, max = node.data):
        return False
    # update min value if we try to move to right
    if node.right and not validate(node.right, min = node.data, max = max):
        return False
    
    return True