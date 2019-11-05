
try:
    raise Exception("Something exception occurred")
except Exception as e:

    # When raising this exception, the structure of the traceback is different.
    # Python thinks a new exception occurred while handling the inner exception and that
    # semantically, these two exceptions are unrelated in their cause.
    # That is to say, the cause of the outer exception is not the inner exception.
    raise Exception("Unrelated exception")
