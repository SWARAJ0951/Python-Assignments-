maximum = lambda a, b, c: a if a >= b and a >= c else (b if b >= c else c)

def main():
    value1 = int(input("Enter the first no: "))
    value2 = int(input("Enter the second no: "))
    value3 = int(input("Enter the third no: "))


    Ret = maximum(value1, value2,value3)

    print("Max value is", Ret)

if __name__ == "__main__":
    main()