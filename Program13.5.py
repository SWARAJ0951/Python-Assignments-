def Marks(m):
    if m >= 75:
        print("Distinction")
    elif m >= 60:
        print("First Class")
    elif m >= 50:
        print("Second Class")
    else:
        print("Fail")

def main():
    m=int(input("enter the marks :"))

    Ret=Marks(m)

if __name__ == "__main__":
    main()