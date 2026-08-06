def Area(Radius ,PI = 3.14):
    Ans = PI * Radius * Radius
    return Ans

def main():
    rad = int(input("Enter the Radius :"))

    Ret = Area(rad)
    
    print(" Area of circle is :",Ret)

    
if __name__ == "__main__":
    main()