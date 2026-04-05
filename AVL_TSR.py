class NodeClass:
    def __init__(self, center_value, left_node = None , right_node = None):
        self.center_value = center_value
        self.left_node = left_node
        self.right_node = right_node

def main():
    node = NodeClass(10)
    node.right_node = NodeClass(20,None,NodeClass(30))

    print("Height of the tree:", calcHeight(node))
    print("Balance Factor of the tree:", calcBF(node))

#should return -1 for null, 0 for leaf, and the height of the tree for non-leaf nodes
def calcHeight(node):
    if node is None:
        return -1
    left_height = calcHeight(node.left_node)
    right_height = calcHeight(node.right_node)
    return 1 + max(left_height, right_height)

#subtract the left height to the right height
def calcBF(node):
    left_height = calcHeight(node.left_node)
    right_height = calcHeight(node.right_node)
    return left_height - right_height

def rotateRight(node):
    new_root = node.left_node
    node.left_node = new_root.right_node
    new_root.right_node = node
    return new_root

def rotateLeft(node):
    new_root = node.right_node
    node.right_node = new_root.left_node
    new_root.left_node = node
    return new_root

def rotateRightLeft(node):
    node.right_node = rotateRight(node.right_node)
    return rotateLeft(node)

def rotateLeftRight(node):
    node.left_node = rotateLeft(node.left_node)
    return rotateRight(node)

def balance(node):
    bf = calcBF(node)
    
    if bf >= 2:  # left heavy
        if calcBF(node.left_node) < 0:  # zig-zag
            return rotateLeftRight(node)
        return rotateRight(node)
    
    if bf <= -2:  # right heavy
        if calcBF(node.right_node) > 0:  # zig-zag
            return rotateRightLeft(node)
        return rotateLeft(node)
    
    return node  # no rebalancing needed

def insert(node, value):
    if node is None:
        return NodeClass(value)
    
    if value < node.center_value:
        node.left_node = insert(node.left_node, value)
    else:
        node.right_node = insert(node.right_node, value)
    
    return balance(node)

def searchVal(node, value):
    if node is None:
        return False
    if node.center_value == value:
        return True
    elif node.center_value > value:
        return searchVal(node.left_node, value)
    else:
        return searchVal(node.right_node, value)

def findLowest(node):
    thisNode = node
    if thisNode.left_node is not None:
        thisNode = thisNode.left_node
        return findLowest(thisNode)
    return thisNode

def findHighest(node):
    thisNode = node
    if thisNode.right_node is not None:
        thisNode = thisNode.right_node
        return findHighest(thisNode)
    return thisNode

if __name__ == "__main__":
    main()