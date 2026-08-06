def AdditionFactors(num):
    sum = 0

    for i in range(1, num ):
        if num % i == 0:
            sum = sum + i

    return sum


def main():
    no = int(input("Enter a number: "))

    result = AdditionFactors(no)

    print("Addition of factors is:", result)


if __name__ == "__main__":
    main()