import string
import re

loremIpsum = open("data.txt", "r")

#exit = False
nbLetters = {}

#for letter in string.ascii_lowercase:
#    nbLetters[letter] = 0

#while not exit:
line = loremIpsum.readline()
#for letter in string.ascii_lowercase:
#    letterOccurences  = re.findall(str(letter), line)
#    nbLetters[letter] += len(letterOccurences)

aOccurences = re.findall("a|A", line)
print(aOccurences)
#    exit = (len(line) == 0)

print(nbLetters)

loremIpsum.close()