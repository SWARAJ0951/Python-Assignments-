def String(Data):
    return len(Data)>5

def main():
    Data = input("Enter the strings separated by space: ").split()

    Result = list(filter(String,Data))

    print("string having length greater then 5 :",Result)

if __name__ == "__main__":
    main()