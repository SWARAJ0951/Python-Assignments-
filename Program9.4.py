def Cube(no):
    cb=no*no*no
    return cb

def main():
    No = int(input("Enter the Number : "))

    Ret = Cube(No)

    print("Cube is: ",Ret)
    
if __name__ == "__main__":
    main()