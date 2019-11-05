

def main():

    # Else clause is not called when exceptions occur.
    try:
        print("Try clause 1")
        raise Exception("Something exceptional occurred.")
    except Exception as e:
        print(f"\t{e}")
    else:
        print("Unreachable code")
    finally:
        print("\tFinally clause 1")

    # Else clause is called when exceptions do not occur and
    # the try clause exits normally.
    try:
        print("Try clause 2")
        print("\tNothing exceptional here.")
    except Exception as e:
        print(e)
    else:
        print("\tElse clause")
    finally:
        print("\tFinally clause 2")

    # Else clause is not called when the try clause exits early from returns.
    try:
        print("Try clause 3")
        print("\tReturning early.")
        return
    except Exception as e:
        print(e)
    else:
        print("\tUnreachable code")
    finally:
        print("\tFinally clause 3")


main()