def Divisble(No):
    return No % 3 == 0 and No % 5 == 0

def main():
    n = int(input("How many Numbers To be added in the list :"))

    Data = []

    for i in range(n):
        num = int(input("Enter the Number :"))
        Data.append(num)

    Result = list(filter(Divisble,Data))

    print("Number divisible by 3 and 5 are :",Result)
    
if __name__ == "__main__":
    main()