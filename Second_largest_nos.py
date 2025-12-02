def second_largest(lst):
    unique_numbers = set(lst)
    unique_numbers = list(unique_numbers)
    unique_numbers.sort()
    return unique_numbers[-2]

def main():
    lst = list(map(int,input("Enter the list:").split()))
    print(second_largest(lst))

if __name__=='__main__':
    main()