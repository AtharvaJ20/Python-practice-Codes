def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def LCM(a,b):
    return (a*b)//GCD(a,b)

def main():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(GCD(a,b))
    print(LCM(a,b))

if __name__=='__main__':
    main()