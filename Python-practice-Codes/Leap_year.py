def leap(Year):
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 ==0:
                print("Leap Year")
            else:
                print("Not a leap Year")
        else:
            print("Leap Year")
    else:
        print("Not a leap year")

def main():
    Year = int(input("Enter the year:"))
    leap(Year)

main()

        