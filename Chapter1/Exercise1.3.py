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

for iteration in range(4):
    line = ""
    for part_of_speech in sentence_structures[random.randint(0, 5)]:
        line += random.choice(part_of_speech) + " "
    print(line)
