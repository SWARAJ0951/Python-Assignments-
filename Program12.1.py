def Ch(ch):
    if ch.lower() in "aeiou":
        print("Vowel")

    else:
        print("Consonant")

def main():
    ch=input("Enter the Alphabet:")

    Ret = Ch(ch)

if __name__ == "__main__":
    main()