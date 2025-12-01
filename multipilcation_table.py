def multiply(n):
    for i in range(0,13):
        i *= n
        print(i)

def main():
    n = int(input("Enter the number:"))
    multiply(n)

if __name__=='__main__':
    main()
