def sleepIn(weekday, vacation):

    if weekday:
        if vacation:
            return True
        return False
    return True

# this is a newly defined method which takes in x as a parameter
def sum3(x):
    # this method outputs our "x" input added with 3
    # after return, method is done
    return x+3
    
    
def div2(x):
    return x/2, 5, 10



# this is our main method
def main():

   '''print("This is the main method")

    #ways to use sum3(22)
    print (sum3(22))

    result = sum3(22)
    print(result)

    #can use variable
    numStudents = 3
    result = sum3(numStudents)
    print(result)

    res = div2(5)
    print(res)'''

    print(sleepIn(True,True))

    
    

                
if __name__ == "__main__":
    main()
