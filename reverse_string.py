def loop(text):
    rev = ""

    for char in text:
        rev = char + rev
    return rev

def main():
    print(loop("Hello"))

if __name__=='__main__':
    main()

