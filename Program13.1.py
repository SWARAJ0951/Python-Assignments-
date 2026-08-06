def Area(length,width):
    area=length*width

    return area


def main():
    len=int(input("Enter the Len:"))
    wid=int(input("Enter the Wid:"))

    Ret=Area(len,wid)

    print("Area of Rectangle is :",Ret)

if __name__ =="__main__":
    main()
    
