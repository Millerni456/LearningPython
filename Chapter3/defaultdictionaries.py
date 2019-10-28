import collections

# To create a default dictionary, we pass a factory function used
# to generate the default value.
# In this case we use the "lambda" statement to create and use that function in-line.
user_defined_tiles = collections.defaultdict(lambda: None)

print(user_defined_tiles["tile_grass"])
print(user_defined_tiles)
