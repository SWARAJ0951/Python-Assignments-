Even = lambda No :(No%2 == 0)

def main():
    No = int(input("Enter the Number :"))

    Ret =Even(No)

    if (Ret == True):
        print("Number is Even")

    else:
        print("Number is Odd ")

if __name__ == "__main__":
    main()