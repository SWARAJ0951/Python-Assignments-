def Even(n):
    for i in range(2,n+1,2):
        print(i)
    

def main():
    n = int(input("Enter the No : "))

    Ret= Even(n)

if __name__ == "__main__":
    main()