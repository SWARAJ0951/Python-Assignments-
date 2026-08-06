def Add(No1,No2):
    sum = No1+No2

    return sum

def main():
    Value1 = int(input("enter the number :"))
    Value2 = int(input("enter the number :"))

    Ret = Add(Value1,Value2)

    print("Addition of Two Numbers is :",Ret)

if __name__ == "__main__":
    main()