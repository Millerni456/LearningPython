print("Hello", "World!")

x = "blue"
y = "green"
z = x

print(x, y, z)

a = True
b = True
c = False
print(a and b)  # outputs True
print(a and c)  # outputs False
print(a or b)  # outputs True
print(a or c)  # outputs True
print(not a)  # outputs False
print(not c)  # outputs True

a = 5
if False:
    pass  # do nothing since this is impossible to execute.
elif a > 4:
    print("a is greater than 4")
else:
    pass  # do nothing since this is impossible to execute.
