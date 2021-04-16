import re

loremIpsum = open("data.txt", "r")


nbWords = 0
exit = False
while not exit:
    line = loremIpsum.readline()
    words = re.split("([\s,.!?:;])", line)
    for word in words:
        test = re.search("^([a-zA-Z\-]+)$", word)
        if test is None:
            continue
        else:
            nbWords += 1
    exit = (len(line) == 0)

print(nbWords)

results = open("data_stats1.txt", "w")
results.writelines(str(nbWords)+"\n")
loremIpsum.close()
results.close()