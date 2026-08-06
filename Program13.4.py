def binary(num):
    bin=" "

    while num > 0:
        remainder = num % 2
        bin = str(remainder) + bin
        num = num // 2

    return bin
    
def main():
    n = int(input("Enter the Number :"))

    Ret = binary(n)

    print("Binary Equivalent :",Ret)

if __name__ == "__main__":
    main()