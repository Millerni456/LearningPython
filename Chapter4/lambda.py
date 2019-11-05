
# The following lines create lambda functions and assign them to objects; however,
# this is considered bad style.
lshift_b10 = lambda num, places=1: num * (10 ** places)
rshift_b10 = lambda num, places=1: num * (10 ** -places)

mynum = 1

print(lshift_b10(mynum, 5))
print(lshift_b10(mynum, 4))
print(lshift_b10(mynum, 3))
print(lshift_b10(mynum, 2))
print(lshift_b10(mynum))
print(mynum)
print(rshift_b10(mynum))
print(rshift_b10(mynum, 2))
print(rshift_b10(mynum, 3))
print(rshift_b10(mynum, 4))
print(rshift_b10(mynum, 5))


# The proper way to use lambdas is by passing them to functions in-line.
def exec_and_print(*nums, transform):
    for num in nums:
        print(transform(num), end=" ")


exec_and_print(3.60874, 3.28, 4.5, 109.38, 20.77, transform=lambda num: num * 10)
