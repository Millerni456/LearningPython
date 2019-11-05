
# The number declared in the for expression is accessible in the else clause
# as well as outside of the for loop.

for number in range(5):
    print(number)
else:
    print("Else: ", number)

print("Outside scope: ", number)
