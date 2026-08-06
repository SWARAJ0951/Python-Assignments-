def Square(no):
    Sq = no * no

    return Sq

def main():
    n = int(input("How many Numbers To be added in the list :"))

    Data = []

    for i in range(n):
        num = int(input("Enter the Number :"))
        Data.append(num)
        
    Result = list(map(Square,Data))

    print(Result)

if __name__ == "__main__":
    main()