def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n - 1)

def main():
    n=int(input("Enter the no: "))

    Ret=Factorial(n)

    print("Factorial of number is :",Ret)

if __name__ == "__main__":
    main()