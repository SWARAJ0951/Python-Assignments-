from functools import reduce

def Min(No1,No2):
    return No1 if No1 < No2 else No2

def main():
    n = int(input("How many Numbers To be added in the list :"))

    Data = []

    for i in range(n):
        num = int(input("Enter the Number :"))
        Data.append(num)

    Result = reduce(Min,Data)

    print("Maximum Number :",Result)

if __name__ == "__main__":
    main()