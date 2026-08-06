def ChkGreater(No1,No2):
    if No1>No2:
        print(No1,"is Greater")
    else:
        print(No2,"is Greater")

def main():
    No1 = int(input("enter first no:"))
    No2 = int(input("enter second no:"))

    Ret = ChkGreater(No1,No2)

if __name__ == "__main__":
    main()
