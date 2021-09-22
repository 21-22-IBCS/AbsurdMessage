def main():

    #using print function to show title and date of assignment
    print("Python Basic Commands Practice")
    print("22 September 2021")

    #assigning var x and y, defined as integers
    x = 99
    y = 14

    #print sum and product of x and y
    print(x+y)
    print(x*y)

    #setting 'a' as number of students which is being added onto for each line. wrapping the integer 'a' as string data type
    a = 20 
    print("There are currently " + str(a) + " number of students in the USG.")
    a = a+60
    print("There are currently " + str(a) + " number of students in the USG.")
    a = a+77
    print("There are currently " + str(a) + " number of students in the USG.")
  

if __name__== "__main__":
    main()
