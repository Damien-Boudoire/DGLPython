import re

#wordLength = int(input("Veuillez entrer un nombre : "))


def incrementEntry(listToEdit, entry):
    if len(listToEdit) <= entry:
        for i in range(len(listToEdit), entry):
            listToEdit.append(0)
        listToEdit.append(1)
    else:
        listToEdit[entry] += 1

loremIpsum = open("data.txt", "r")
count = []
exit = False
while not exit:
    line = loremIpsum.readline()
    words = re.split("([\s,.!?:;])", line)
    wordLength = 1
    thereIsTaller = True
    while thereIsTaller:
        thereIsTaller = False
        for word in words:
            test1 = re.search("^([a-zA-Z\-]{" + str(wordLength) + "})$", word)
            test2 = re.search("^([a-zA-Z\-]{" + str(wordLength) + "})[a-zA-Z\-]", word)

            if test2 is not None:
                thereIsTaller = True

            if test1 is None:
                continue
            else:
                incrementEntry(count, wordLength)
        wordLength += 1
    exit = (len(line) == 0)

print(count)

results = open("data_stats2.txt", "w")
for n in count:
    results.write(str(n)+"\n")



loremIpsum.close()