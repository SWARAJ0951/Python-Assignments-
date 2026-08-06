def Fun(num):
    while num >1:
        num = num - 1
        print(num)

def main():
    value = int(input("enter the number "))

    Ret = Fun(value)

if __name__ == "__main__":
    main()