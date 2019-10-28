def main():
    print("max: ", getmax(5, 10)) # correctly typed - no error at all.
    print("max: ", getmax("hello", 3)) # incorrectly typed - error only preset at runtime


def getmax(a, b):
    if a >= b:
        return a
    else:
        return b


main()
