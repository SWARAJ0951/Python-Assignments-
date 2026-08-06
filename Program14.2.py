Cube = lambda no :no**3

def main():
    no = int(input("Enter the Number : "))

    Ret = Cube(no)

    print(f"Cube of {no} is {Ret}")

if __name__ == "__main__":
    main()