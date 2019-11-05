
# The else clause executes when the loop exits naturally, or if it never enters.

index = 0
while index < 10:
    index += 1
else:
    print("Else executed")

while False:
    pass
else:
    print("Else executed")

# However if we break (or return) from inside the loop, the else is skipped.
while True:
    break
else:
    print("Unreachable code")

# The else clause is also skipped when encountering exceptions
try:
    while True:
        raise Exception("Loop exited unexpectedly")
    else:
        print("Unreachable code")
except Exception as e:
    print(e)
