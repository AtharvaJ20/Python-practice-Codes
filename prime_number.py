import math

def prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2 , n):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"


#optimised code

def isprime(n):
    if n <= 1:
        return "Not Prime"

    for i in range(2, int(math.sqrt(n)+1)):
        if n % 2 == 0:
            return "Not Prime"

    return "Prime"

def main():
    print(prime(5))
    print(isprime(3))

main()


