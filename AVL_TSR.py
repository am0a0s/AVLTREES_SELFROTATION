def main():

    print("AVL Trees & Rotations inspired Self-Balancing Recursive Structure in Python")

    collection = []
    area = int(input("Enter the number of values you will input: "))

    for x in range(area):
        number = int(input("Enter Number: "))
        collection.append(number)


        print("Currently in the collection:", collection)

if __name__ == "__main__":
    main()