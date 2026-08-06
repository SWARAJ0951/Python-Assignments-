def reverse(num):
    rev = 0

    while num>0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev

def main():
    n = int(input("Enter the Number :"))

    Ret = reverse(n)

    print("Reverse is :",Ret)

if __name__ == "__main__":
    main()