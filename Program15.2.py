def CheckEven(No):
    return (No % 2 == 0)

def main():
    n = int(input("How many Numbers To be added in the list :"))

    Data = []

    for i in range(n):
        num = int(input("Enter the Number :"))
        Data.append(num)

    print("Input Data is :",Data)

    FData = list(filter(CheckEven,Data))

    print("Data After filter : ",FData)

if __name__ == "__main__":
    main() 