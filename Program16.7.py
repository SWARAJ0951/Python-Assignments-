def Fun(No):
    if No%5==0:
        return True
    else:
        return False
    
def main():
    value = int(input("Enter the Number : "))

    Ret = Fun(value)

    if Ret == True:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()