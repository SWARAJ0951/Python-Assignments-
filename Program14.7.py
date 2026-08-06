Div = lambda No :(No%5 == 0)

def main():
    No = int(input("Enter the Number :"))

    Ret =Div(No)

    if (Ret == True):
        print("Number is Divisble by 5")

    else:
        print("Number is Not Divisible by 5")

if __name__ == "__main__":
    main()