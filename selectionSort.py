def sort():
    numList = [2,3,30,8,5]
    print(numList)

    minimum = numList[0]
    x = 0


    
    for a in range(len(numList)-1):
        minimum = numList[a]
        x = a
        #check the next number each time
        for i in range(a+1,len(numList)):
            #print(numList[a])
            if (numList[i]) < minimum:
                minimum = (numList[i])
                x = i
                #print(minimum)
        #to swap
        temp = numList[a]
        numList[a] = numList[x]
        numList[x] = temp

    return numList

def main():

    print(sort())
    


if __name__ == "__main__":
    main()
