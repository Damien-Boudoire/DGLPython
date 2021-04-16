import string
import re

import matplotlib.pyplot as pyplot

loremIpsum = open("data.txt", "r")


bigrams = {}
for firstLetter in string.ascii_lowercase:
    bigrams[firstLetter] = {}
    for secondLetter in string.ascii_lowercase:
        bigrams[firstLetter][secondLetter] = 0

bigramsProb = bigrams.copy()

nbLine = 0
exit = False
while not exit:
    line = loremIpsum.readline()
    for firstLetter in string.ascii_lowercase:
        for secondLetter in string.ascii_lowercase:
            letterOccurences  = re.findall("(" + firstLetter +"|" + firstLetter.upper() +")"
                                           +"(" + secondLetter + "|" + secondLetter.upper() + ")", line)
            bigrams[firstLetter][secondLetter] += len(letterOccurences)
    print(str(nbLine) + " read")
    nbLine += 1
    exit = (len(line) == 0)

print(bigrams)
loremIpsum.close()


for firstLetter in bigrams:
    total = sum(bigrams[firstLetter].values())
    if total == 0:
        continue
    for secondLetter in bigrams[firstLetter]:
        bigramsProb[firstLetter][secondLetter] = bigrams[firstLetter][secondLetter] / total


for firstLetter in bigramsProb:
    pyplot.plot(bigramsProb[firstLetter].keys(), bigramsProb[firstLetter].values())

results = open("data_stats4.txt", "w")
count = 0
for firstLetter in string.ascii_lowercase:
    for secondLetter in string.ascii_lowercase:
        results.write(str(bigramsProb[firstLetter][secondLetter])+"\n")
        print(firstLetter + " , " + secondLetter)
        count += 1

print(count)
pyplot.grid()
pyplot.grid(linestyle = "dotted", axis="y")
pyplot.show()