def prime(n):
    if n < 1:
        return "Not Prime"
    
    for i in range(2 , n):
        if i%i == 0:
            return "Not Prime"
    
    return "Prime"

print(prime(5))


#