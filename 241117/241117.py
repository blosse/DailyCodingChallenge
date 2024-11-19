# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), # which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
#
# This one was a bit of a bastard...

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    ret = []
    def dfs(node):
        if not node:
            ret.append("#")
            return ret
        ret.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(node)
    return ",".join(ret)

def deserialize(serial):
    if not serial:
        return None

    nodes = serial.split(',')
    def dfs():
        if nodes:
            index = nodes.pop(0)
            if index == '#':
                return None
            node = Node(index)
            node.left = dfs()
            node.right = dfs()
            return node

    return dfs()

node1 = Node('root', Node('left', Node('left.left')), Node('right'))
node2 = Node('root', Node('left', Node('left.left')), Node('right', Node('right.left')))
node3 = Node('root', Node('left'), Node('right', Node('right.left'), Node('right.right')))


assert deserialize(serialize(node1)).left.left.val == 'left.left' # Pyright marks this line as erroneous but it seems to work?
assert deserialize(serialize(node2)).right.val == 'right' # Pyright marks this line as erroneous but it seems to work?
assert deserialize(serialize(node3)).right.left.val == 'right.left' # Pyright marks this line as erroneous but it seems to work?
