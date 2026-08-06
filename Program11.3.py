def Number(num):
    sum = 0

    while num>0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    return sum

def main():
    n = int(input("Enter the Number :"))

    Ret = Number(n)

    print("Summation is :",Ret)

if __name__ == "__main__":
    main()
