import collections
import string
import sys


words = collections.defaultdict(int)
strip_characters = string.whitespace + string.punctuation + string.digits
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip_characters)
                if len(word) > 2:  # filter out words like "a", or "an"
                    words[word] += 1

for word, count in sorted(words.items(), key=lambda item: item[1]):
    print("'{0}' occurs {1} time(s)".format(word, count))
