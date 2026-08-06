def Odd(n):
    for i in range(1,n+1,2):
        print(i)
    

def main():
    n = int(input("Enter the No : "))

    Ret= Odd(n)

if __name__ == "__main__":
    main()