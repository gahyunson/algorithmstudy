# --- Directions
# Given the root node of a tree, return
# an array where each element is the width
# of the tree at each level.
# --- Example
# Given:
#     0
#   / |  \
# 1   2   3
# |       |
# 4       5
# Answer: [1, 3, 2]

def levelWidth(root):
    counters = [0]
    arr = [root, 's']

    while len(arr) > 1 :
        node = arr.pop(0)

        # pull out value 's',
        # 's' == we've hit a new row 
        if node == 's':
            counters.append(0)
            # and add 's' back to the very end of the array
            arr.append('s')
        else :
            # add all the childrens of the current node
            # have to use 'extend' method -> to add each child node individually
            arr.extend([child for child in node.children])
            # have to count the row location!
            counters[len(counters)-1]+=1
    
    return counters