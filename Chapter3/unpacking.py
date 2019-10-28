
# A star on the left-hand side of assignment creates a starred assignment target.
# This performs sequence unpacking.
map = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
a, b, c, *rest = map.items()

print(a)
print(b)
print(rest)

# Where supported maps can be unpacked using two stars, this can be done to supply
# keyword arguments (**kwargs)
print("{a}, {b}, {c}, {d}, {e}".format(**map))
