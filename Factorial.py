def fact_loop(n):
    result = 1

    for i in range(1,n+1):
        result *= i 
    return result

def fact_recursion(n):
    if n==0 or n==1:
        return 1
    return n * fact_recursion(n-1)

def main():
    print(fact_loop(6))
    print(fact_recursion(3))

if __name__=='__main__':
    main()