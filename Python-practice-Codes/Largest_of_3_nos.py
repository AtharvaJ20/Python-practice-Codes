def largest(a,b,c):
    if a>b and a>c:
        print("A is largest")
    elif b>c:
        print("B is largest")
    else:
        print("C is largest")

def main():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))
    largest(a,b,c)

main()