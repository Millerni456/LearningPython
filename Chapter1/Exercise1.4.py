import random

articles = ["the"]
adjectives = ["spoiled", "blue", "happy", "sweet", "bitter", "incredible", "only"]
nouns = ["cat", "dog", "man", "woman", "cantaloupe", "bot", "computer", "tea", "bedroom", "cow", "moon", "car"]
verbs = ["sang", "ran", "jumped", "was destroyed", "drank", "ate", "drove", "painted"]
adverbs = ["loudly", "quietly", "well", "badly", "impressively", "directly"]
prepositions = ["over", "by", "without", "with", "near", "away from", "in", "for"]

sentence_structures = [
    [articles, nouns, verbs, adverbs],
    [articles, nouns, verbs],
    [articles, nouns, verbs, prepositions, articles, nouns],
    [articles, nouns, verbs, adverbs, prepositions, articles, nouns],
    [articles, nouns, verbs, adverbs, prepositions, articles, adjectives, nouns],
    [articles, adjectives, nouns, verbs, adverbs, prepositions, articles, nouns]
]

while True:
    try:
        response = input("enter a number between 1 and 10 or Enter to quit: ")
        if not response:
            break
        number = int(response)
        if 1 <= number <= 10:
            for iteration in range(number):
                line = ""
                for part_of_speech in sentence_structures[random.randint(0, 5)]:
                    line += random.choice(part_of_speech) + " "
                print(">", line)
        else:
            print("The input is not within 1 and 10")
    except ValueError as err:
        print("The input is not an integer")
    except (EOFError, KeyboardInterrupt) as err:
        break
