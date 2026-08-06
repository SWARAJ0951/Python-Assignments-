def Fun(No):
    if No>0:
        print("positive number")

    elif No<0:
        print("Negative number")

    elif No == 0:
        print("Zero")

def main():
    value = int(input("Enter the Number : "))

    Ret = Fun(value)

if __name__ == "__main__":
    main()