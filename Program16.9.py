def Fun(n):
    num = 2
    for i in range(n):
        print(num)
        num=num+2

def main():
    value = int(input("Enter the Number : "))

    Ret = Fun(value)

if __name__ == "__main__":
    main()