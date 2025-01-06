# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

# Node class
class Node:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

def isUnivalTree(root):
    
    if (not root):
        return True

    if (root.left != None and root.val != root.left.val):
        return False

    if (root.right != None and root.val != root.right.val):
        return False

    return isUnivalTree(root.left) and isUnivalTree(root.right)

def countUnivalTrees(root):
    count_left = 0
    count_right = 0

    if (not root):
        return 1

    if (root.left):
        count_left = countUnivalTrees(root.left )

    if (root.right):
        count_right = countUnivalTrees(root.right)

    if isUnivalTree(root):
        return 1 + count_left + count_right

    return count_left + count_right

# Testing

#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1


node1 = Node(1, Node(1), Node(1))

node2 = Node(0)

node3 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

print(countUnivalTrees(node1))
print(countUnivalTrees(node2))
print(countUnivalTrees(node3))

    


