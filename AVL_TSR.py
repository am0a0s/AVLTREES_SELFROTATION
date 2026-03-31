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
def calcHeight(center_value, left_node, right_node):
    if center_value is None:
        return -1
    if left_node is None and right_node is None:
        return 0
    return calcHeight

#subtract the left height to the right height
def calcBF(calcHeight):
    pass
    balance_factor = 0

def rotate(center_value, left_node, right_node):
    calculateHeightBF(center_value, left_node, right_node)
    #perform rotations here

 #def insert(value):

#if __name__ == "__main__":
    main()