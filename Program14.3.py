Max = lambda No1, No2: No1 if No1 > No2 else No2

def main():
    value1 = int(input("Enter the first no: "))
    value2 = int(input("Enter the second no: "))

    Ret = Max(value1, value2)

    print("Max value is", Ret)

if __name__ == "__main__":
    main()