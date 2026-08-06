def Divisible(no):
    if no%3 == 0 and no%5 == 0:
        print("Divisible By 3 and 5 ")
    else:
        print("Not Divisible By 3 and 5")


def main():
    No = int(input("Enter the Number :"))

    Ret = Divisible(No)

if __name__ == "__main__":
    main()