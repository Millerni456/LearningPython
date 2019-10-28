import os

people = {"alice": 23, "bob": 40, "carl": 28, "donald": 67, "elena": 43, "fred": 37, "grace": 32, "helen": 30}

thirties = {name: age for name, age in people.items() if 30 <= age <= 39}

for key, value in thirties.items():
    print(f"{key} is {value} years old.")

print("-" * 30)

older = {name.capitalize(): age + 1 for name, age in people.items() if 30 <= age <= 39}

for key, value in older.items():
    print(f"{key} is {value} years old.")

print("-" * 30)

file_sizes = {name: os.path.getsize(name) for name in os.listdir(".") if os.path.isfile(name)}
print(file_sizes)


print("-" * 30)

# Note that when inverting a dictionary with a dictionary comprehension values may be overwritten.
# In the below example alice is no longer present in the dictionary.
people["isabella"] = 23
inverted_people = {age: name for name, age in people.items()}
print(inverted_people)
