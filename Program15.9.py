from functools import reduce

def Product(No1 ,No2):
    sum = 0 
    sum = No1 * No2
    return sum

def main():
    n = int(input("How many Numbers To be added in the list :"))

    Data = []

    for i in range(n):
        num = int(input("Enter the Number :"))
        Data.append(num)

    Result = reduce(Product,Data)

    print("Product of Numbers is :",Result)
    
if __name__ == "__main__":
    main()