def Perfect(num):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum = sum + i

    if sum == num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

def main():
    n = int(input("Enter the Number :"))

    Ret = Perfect(n)

if __name__ == "__main__":
    main()