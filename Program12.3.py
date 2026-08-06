def Cal(no1,no2):
    add=no1+no2
    print("Addition is:",add)

    sub=no1-no2
    print("Subtraction is :",sub)

    mul=no1*no2
    print("Multiplication is :",mul)

    div=no1%no2
    print("Division is :",div)

def main():
    no1=int(input("Enter the Number : "))
    no2=int(input("Enter the Number :"))

    Ret = Cal(no1,no2)

if __name__ == "__main__":
    main()