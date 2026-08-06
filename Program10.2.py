def sum(n):
    sum=0
    for i in range(1,n+1):
        sum = sum + i
    return sum

def main():
    no = int(input("enter the number :"))

    Ret=sum(no)

    print(Ret)

if __name__ == "__main__":
    main()

