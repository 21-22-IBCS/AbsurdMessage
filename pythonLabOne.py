def coffeeShop():
    name = input("Welcome to Sasha's Qwafee! What is your name?")
    order = input("What is your order?")
    print("\n")
    print("Alright " + name + ", we'll have that "+ order +" right out for you.")

    receipt = "\nYour receipt:" + "\nCustomer:"+ name + "\nOrder:"+ order + "\nOrder #: 1"
    return receipt

    
def palindrome(x):


    print("\n")
    backward = ""

    for i in range(len(x)):
        backward = backward + x[-i-1]

    if x == backward:
        return True
    else:
        return False


def main():

    typedReceipt = coffeeShop()
    print(typedReceipt)
    print("\n")


    word = input("Type a palindrome:")
    print(palindrome(word))
 
if __name__ == "__main__":
    main()
