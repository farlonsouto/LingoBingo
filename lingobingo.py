import random

with open("buzzwords.lingo", "r") as f:
    lines = f.readlines()

buzzwords = []
for line in lines:
    split = line.split(",")
    for word in split:
        if word != "\n":
            buzzwords.append(word)

boardWords = random.sample(buzzwords, 9)

print(boardWords)
