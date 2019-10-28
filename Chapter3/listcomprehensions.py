import math

evens = [item for item in range(0, 10) if item % 2 == 0]
print(evens)

odds = [item for item in range(0, 10) if item % 2 == 1]
print(odds)

powers_of_two = [math.trunc(math.pow(2, item)) for item in range(0, 10)]
print(powers_of_two)

evens_squared = [item * item for item in [item for item in range(0, 10) if item % 2 == 0]]
print(evens_squared)

