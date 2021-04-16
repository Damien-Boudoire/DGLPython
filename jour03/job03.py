import re

wordLength = int(input("Veuillez entrer un nombre : "))

loremIpsum = open("data.txt", "r")
exit = False
nbWords = 0

while not exit:
    line = loremIpsum.readline()
    words = re.split("([\s,.!?:;])", line)
    for word in words:
        test = re.search("^([a-zA-Z\-]{" + str(wordLength) + "})$", word)
        if test is None:
            continue
        else:
            nbWords += 1
    exit = (len(line) == 0)

print(nbWords)
loremIpsum.close()