def main():
    #Everything indented is part of main method

    #Data types: print, str, int, 





    print ("Hi hi hi")
    
    student1 = "Sasha"
    student2 = "Kamalani"
    print(student1)
    print(student2)

    print(student1 + " and " + student2)
    #Strings can be concatenated but not use 'u' or '*'
    #print(student1-students2)

    numPlants = 112
    print(numPlants+10)
    #int types can't concatenate with str types
    #print("Mr. Considine has " + numPlants + "plants")
    print("Mr. Considine has " + str(numPlants) + " plants")

    awFounded = "1884"
    current = 2021

    print("Years since Annie Wright has been founded:")
    print(current - int(awFounded))





    #Floats are numbers that aren't integers
    w = -11.444444444444
    x = 2.5
    y = -3.01
    z = 7.0
    print(x + x)
    print(type(x))
    print(type(x+x))

    x = 7
    y = 2
    print(7/2)
    print(x/y)
    print(type(x/y))

    #Booleans are either True or False
    classToday = True
    day = "Wednesday"
    if day == "Thursday":
        classToday = False
    print(classToday)
    
        


    

if __name__ == "__main__":
    main()
