from functools import reduce

def Add(No1,No2):
    return No1 + No2

def main():
    n = int(input("How many Numbers To be added in the list :"))

    Data = []

    for i in range(n):
        num = int(input("Enter the Number :"))
        Data.append(num)

    Result = reduce(Add,Data)

    print("Summation of Numbers is :",Result)

if __name__ == "__main__":
    main()