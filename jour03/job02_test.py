import re

loremIpsum = open("data.txt", "r")


nbWords = 0
exit =False
while not exit:
    line = loremIpsum.readline()
    words = re.split("[\s,.!?:;]+", line)
    for word in words:
        test = re.search("^.*[^a-zA-Z\-]+.*$", word)
        if test is None:
            continue
        else:
            print(str(word))
            nbWords += 1
    if len(line) == 0:
        exit = True
print(nbWords)