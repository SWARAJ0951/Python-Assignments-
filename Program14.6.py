Odd = lambda No :(No%2 != 0)

def main():
    No = int(input("Enter the Number :"))

    Ret =Odd(No)

    if (Ret == True):
        print("Number is Odd")

    else:
        print("Number is Even ")

if __name__ == "__main__":
    main()