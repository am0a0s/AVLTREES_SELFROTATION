class NodeClass: #node class for AVL tree that includes the center value, left node, and right node
    def __init__(self, center_value, left_node = None , right_node = None):
        self.center_value = center_value #root node value
        self.left_node = left_node #left child node
        self.right_node = right_node #right child node

def main(): #where everything is executed
    rootNode = None
    collection = []

    print("AVL Inspired Self-Balancing Tree")
    while True: #while loop for user input with a 'p' condition to break loop
        userInput = input("Enter a number (or enter 'p' to stop): ")
        if userInput == 'p':
            break
        collection.append(int(userInput))
        rootNode = insert(rootNode, collection[-1])
        DispCVHTBF(rootNode)
        collection.clear()

    NumberSearch(rootNode)
    LowestAndHighest(rootNode)

#recrsively calculates the height of each node and returns the maximum height of the tree
def calcHeight(node):
    if node is None:
        return -1
    left_height = calcHeight(node.left_node)
    right_height = calcHeight(node.right_node)
    return 1 + max(left_height, right_height)

#subtract the left side height from the right side height
def calcBF(node):
    left_height = calcHeight(node.left_node)
    right_height = calcHeight(node.right_node)
    return left_height - right_height

#rotates the tree to the right and returns the new root node (left_node of the original root will be the new root)
def rotateRight(node):
    new_root = node.left_node
    node.left_node = new_root.right_node
    new_root.right_node = node
    return new_root

#rotates the tree to the left and returns the new root node (right_node of the original root will be the new root)
def rotateLeft(node):
    new_root = node.right_node
    node.right_node = new_root.left_node
    new_root.left_node = node
    return new_root

#same logic with the rotateRight but it handles the zig-zag structure of trees
def rotateRightLeft(node):
    node.right_node = rotateRight(node.right_node)
    return rotateLeft(node)

#same logic with the rotateLeft but it handles the zig-zag structure of trees
def rotateLeftRight(node):
    node.left_node = rotateLeft(node.left_node)
    return rotateRight(node)

#where the balancing happens, it checks the balance factor of the node and decides which rotation to perform based on the balance factor and the structure of the tree
def balance(node):
    bf = calcBF(node)
    
    if bf >= 2:  # left side heavy
        if calcBF(node.left_node) < 0:  # zig-zag
            return rotateLeftRight(node)
        return rotateRight(node) #not zig-zag, just left side heavy
    
    if bf <= -2:  # right side heavy
        if calcBF(node.right_node) > 0:  # zig-zag
            return rotateRightLeft(node)
        return rotateLeft(node) #not zig-zag, just right side heavy
    
    return node  # no rebalancing needed

#inserts a new value into the tree and then immediately balances it after insertion. (finds the correct position for the new value and calls balance func to balance the tree)
def insert(node, value):
    if node is None:
        return NodeClass(value)
    
    if value < node.center_value: #is the new value less than the current node's value? if so, go left
        node.left_node = insert(node.left_node, value)
    else:
        node.right_node = insert(node.right_node, value)
    
    return balance(node)

#searches for whatever value is inputed by the user adn traverses the tree based on the input value and the current node's value
def searchVal(node, value):
    if node is None:
        return False
    if node.center_value == value:
        return True
    elif node.center_value > value:
        return searchVal(node.left_node, value)
    else:
        return searchVal(node.right_node, value)

#Traverse left until no more left nodes exist. 
def findLowest(node):
    thisNode = node
    if thisNode.left_node is not None:
        thisNode = thisNode.left_node
        return findLowest(thisNode)
    return thisNode

#Traverse right until no more right nodes exist. 
def findHighest(node):
    thisNode = node
    if thisNode.right_node is not None:
        thisNode = thisNode.right_node
        return findHighest(thisNode)
    return thisNode

#display the current center value, height of the tree, and balance factor of the tree after each insertion
def DispCVHTBF(rootNode):
    print("\nCurrent Center Value:", rootNode.center_value)
    print("Height of the tree:", calcHeight(rootNode))
    print("Balance Factor of the tree:", calcBF(rootNode))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#display the lowest and highest values in the tree after all insertions are done
def LowestAndHighest(rootNode):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(">>Lowest Number<<")
    print("Lowest value in the tree:", findLowest(rootNode).center_value)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(">>Highest Number<<")
    print("Highest value in the tree:", findHighest(rootNode).center_value)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#searches for the user inputed value and displays whether it was found in the tree or not
def NumberSearch(rootNode):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(">>Search a Number<<")
    numSearch = int(input("Enter a value to search: "))
    if searchVal(rootNode, numSearch):
        print("Value found in the tree.")
        return True
    else:
        print("Value not found in the tree.")
        return False
    
#standard Python entry-point pattern
if __name__ == "__main__":
    main()