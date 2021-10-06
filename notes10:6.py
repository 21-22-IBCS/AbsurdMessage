

def main():

    school = "Annie Wright"
    print(school)

    #individual characters can be indexed
    print(school[3])
    print(school[10])

    #substrings can be indexed as well
    print(school[3:8])
    print(school[:5])
    print(school[7:])
    print(school[-1])

    print("\n\n\n")
    #loop through a string to iterate through its characters
    for i in range(12):
        print (school[-i-1])

    #palindrone lab hint: loop through to print out -i

    print("\n\n\n")
    #can loop words and not just numbers
    weather = "rain"
    for i in range(len(weather)):
        print(2**i)
    
if __name__ == "__main__":
    main()
