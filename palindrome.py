#Palindrome

def using_slicing(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


def using_loop(text):
    rev = ''

    for char in text:
        rev = char + rev

    if rev == text:
        print("Palindrome")
    else:
        print("Not Palindrome")

    #return rev


def using_inbuilt(text):
    if text == ''.join(reversed(text)):
        print("Palindrome")
    else:
        print("Not Palindrome")


def main():
    text = input("Enter the string: ")
    using_slicing(text)
    using_loop(text)
    using_inbuilt(text)

if __name__=='__main__':
    main()