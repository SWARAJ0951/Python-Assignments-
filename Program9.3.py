def Square(no):
    Sq=no*no
    return Sq

def main():
    No = int(input("Enter the Number : "))

    Ret = Square(No)

    print("Square is: ",Ret)
if __name__ == "__main__":
    main()