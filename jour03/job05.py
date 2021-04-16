import string
import re

import matplotlib.pyplot as pyplot

loremIpsum = open("data.txt", "r")

exit = False
nbLetters = {}

for letter in string.ascii_lowercase:
    nbLetters[letter] = 0

while not exit:
    line = loremIpsum.readline()
    for letter in string.ascii_lowercase:
        letterOccurences  = re.findall(letter+"|"+letter.upper(), line)
        nbLetters[letter] += len(letterOccurences)

    exit = (len(line) == 0)

print(nbLetters)
loremIpsum.close()

pyplot.bar(range(len(nbLetters)), nbLetters.values())
pyplot.grid(linestyle = "dotted", axis="y")
pyplot.xticks(range(len(nbLetters)), nbLetters.keys())
pyplot.show()