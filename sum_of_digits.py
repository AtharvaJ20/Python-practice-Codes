def sum(n):
    sum = 0

    while n > 0:
        digit = n % 10
        sum += digit
        n//=10
    return sum

def main():
    n = int(input("Enter the number:"))
    print(sum(n))

if __name__=='__main__':
    main()