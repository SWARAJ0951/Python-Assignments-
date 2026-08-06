def Number(num):
    count = 0

    while num!= 0:
        num = num // 10
        count = count + 1

    print("Number of digits =",count)

def main():
    n = int(input("Enter the Number : "))

    Ret=Number(n)

if __name__ == "__main__":
    main()