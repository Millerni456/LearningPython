MyGlobal = 1


# This function creates a variable that masks the variable in the outer scope
def shadow_global():
    MyGlobal = 2
    print(MyGlobal)


# This function modifies the variable in the outer scope
def modify_global():
    global MyGlobal
    MyGlobal = 3
    print(MyGlobal)


# Nonlocal cannot be used to modify globals.
# However, it can be used to modify nonlocal variables from within nested functions.
def modify_nonlocal():
    x = 10

    def inner1():
        x = 20
        print(f"inner: x={x}")

    def inner2():
        nonlocal x
        x = 30
        print(f"inner: x={x}")

    inner1()
    print(f"outer: x={x}")
    inner2()
    print(f"outer: x={x}")


def main():
    shadow_global()
    print(MyGlobal)

    modify_global()
    print(MyGlobal)

    modify_nonlocal()


main()
