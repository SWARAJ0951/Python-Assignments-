from Arithmetic import *

def main():
    print("Enter First number :")
    Value1=int(input())

    print("Enter Second number :")
    Value2=int(input())

    Ret = Add(Value1 , Value2)
    print("Addition Is : ",Ret)

    Ret = Sub(Value1,Value2) 
    print("Substraction Is : ",Ret)

    Ret = Mult(Value1,Value2) 
    print("Multiplication Is : ",Ret)

    Ret = Div(Value1,Value2) 
    print("Divison Is : ",Ret)

if __name__ == "__main__":
    main()