
# If some outer exception is caused as a direct result of some inner exception,
# then they should be chained by used the from keyword.
# This allows the outer exception to be more descriptive than the inner exception,
# which may be more general.

try:
    try:
        raise IOError("I/O Error while reading PNG file.")
    except Exception as cause:
        print(f"Handling exception: {cause}")
        raise Exception("Module Level Exception - Asset Error") from cause
    finally:
        print("Inner finally")
except Exception as cause:
    print(f"Exception found: {cause}")
    raise Exception("Application Level Exception - Game Error") from cause
finally:
    print("Outer finally")