def fact(n):
    result = 1

    for i in range(1,n+1):
        result *= i 
    print(result)

def main():
    fact(6)

main()