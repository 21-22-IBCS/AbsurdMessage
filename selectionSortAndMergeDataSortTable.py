import time
import random

#20 digits

def selectionSort(li):
    sortedList = []
    while len(li) > 0:
        minE = li[0]
        for i in range(len(li)):
            if li[i] < minE:
                minE = li[i]
        li.pop(li.index(minE))
        sortedList.append(minE)

    return sortedList

def mergeSort(li2):
    if len(li2) > 1:
        m = len(li2)//2
        left = li2[:m]
        right = li2[m:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li2[k] = left[i]
                i += 1
            else:
                li2[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            li2[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            li2[k] = right[j]
            j += 1
            k += 1

def main():

    #List = 
    x = [100,200,300,400,500]

    nestedList=[[100],
                [200],
                [300],
                [400],
                [500]]
    for n in x:
        listOfDifferences = []
        index = int((n/100)-1)

        for i in range(10):

            test1 = []
            for i in range(n):
                    test1.append(random.randint(1,n))

            start = time.time()
            result = selectionSort(test1)
            stop = time.time()
            difference = stop - start
            listOfDifferences.append(difference)

        total = 0
        for dif in listOfDifferences:
            total = total + dif
        avgTime = total/10
        
        
        nestedList[index].append(avgTime)
        listOfDifferences = []

        for i in range(10):

            test1 = []
            for i in range(n):
                    test1.append(random.randint(1,n))

            start = time.time()
            mergeSort(test1)
            stop = time.time()
            difference = stop - start
            listOfDifferences.append(difference)

        total = 0
        for dif in listOfDifferences:
            total = total + dif
        avgTime = total/10
        nestedList[index].append(avgTime)
       
    print("\n")
    print("|  n  | Selection Sort Average Time (sec) | Merge Sort Average Time (sec) |")
    for item in nestedList:
        
        print("|",item[0],"|",
            item[1]," "*(32-len(str(item[1]))),"|",
            item[2]," "*(28-len(str(item[2]))),"|")
            

    #":" + item[0] + ":" + " "*(9-len(item[0])       " "*(9-len(item[0]))       " "*(13-len(item[1])
          
        
if __name__ == "__main__":
    main()
