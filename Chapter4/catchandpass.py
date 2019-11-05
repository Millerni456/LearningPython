
try:
    try:
        raise Exception("Something exception occurred")
    except Exception as e:
        print(f"Handling exception: {e}")
        # When re-raising the exception like this, the following line is added to the traceback
        raise e
    finally:
        print("Inner finally")
except Exception as e:
    print(f"Exception found: {e}")
    # When re-raising the exception like this, we are simply passing it without modifying the traceback
    raise
finally:
    print("Outer finally")
