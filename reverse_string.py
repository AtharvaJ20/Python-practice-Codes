def loop(text):
    rev = ""

    for char in text:
        rev = char + rev
    return rev

def built_in(text):
    rev = "".join(reversed(text))
    return rev


def main():
    print(loop("Hello"))
    print(built_in("Hello"))

if __name__=='__main__':
    main()

