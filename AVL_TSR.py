def main():

    print("AVL Trees & Rotations inspired Self-Balancing Recursive Structure in Python")

    collection = []
   
    #rough visualization of what i would want to happen, is this pseudocode?
    numVal = int(input("Enter the number of values you will input: "))

    for x in range(numVal):
        number = int(input("Enter Number: "))
        collection.append(number)
        node(number)


        print("Currently in the collection:", collection)

#supposedly the node 
def node(value): #would it be better to handle the value indivudally then the main function? or is this fine?
    center_value = None
    left_node = None
    right_node = None
    
    if value > center_value:
        right_node = value
    else:
        left_node = value

    rotate(center_value, left_node, right_node)

#must be the complete calculation for height and bf
def calculateHeightBF(center_value, left_node, right_node):
    calcHeight(center_value, left_node, right_node)
    calcBF(center_value, left_node, right_node)
    return calculateHeightBF

#should return -1 for null, 0 for leaf, and the height of the tree for non-leaf nodes
def calcHeight(node):
    if node is None:
        return -1
    left_height = calcHeight(node.left_node)
    right_height = calcHeight(node.right_node)
    return 1 + max(left_height, right_height)

#subtract the left height to the right height
def calcBF(calcHeight):
    pass
    balance_factor = 0

def rotate(center_value, left_node, right_node):
    calculateHeightBF(center_value, left_node, right_node)
    #perform rotations here

 #def insert(value):


 class NodeClass:
    def __init__(self, center_value, left_node = None , right_node = None):
        self.center_value = center_value
        self.left_node = left_node
        self.right_node = right_node

#if __name__ == "__main__":
    main()