import random
import string


def getNbWords(): #job2
    stat1 = open("data_stats1.txt", "r")
    nbWords = int(stat1.readline())
    stat1.close()
    return nbWords

def getNbWordsByLength(): #job8
    stat2 = open("data_stats2.txt", "r")
    nbWordsByLength = []
    exit = False
    line = stat2.readline()
    while not exit:
        nbWordsByLength.append(int(line))
        line = stat2.readline()
        exit = (len(line) == 0)
    stat2.close()
    return nbWordsByLength

def getNbFirstLetter(): #job13
    stat3 = open("data_stats3.txt", "r")
    nbFirstLetter = {}
    for letter in string.ascii_lowercase:
        line = stat3.readline()
        nbFirstLetter[letter] = int(line)
    stat3.close()
    return  nbFirstLetter

def getBigrams(): #job21
    stat4 = open("data_stats4.txt", "r")
    bigrams = {}
    for alpha in string.ascii_lowercase:
        bigrams[str(alpha)] = {}
        for beta in string.ascii_lowercase:
            line = stat4.readline()
            bigrams[str(alpha)][str(beta)] = float(line)
    stat4.close()
    return bigrams

nbWords = getNbWords()
nbWordsByLength = getNbWordsByLength()
nbFirstLetter = getNbFirstLetter()
bigrams = getBigrams()

probaLength = []
for nb in nbWordsByLength:
    probaLength.append(nb / nbWords)

probaStart = {}
for alpha in string.ascii_lowercase:
    probaStart[alpha] = nbFirstLetter[alpha] / nbWords

#print("sum(probaLength) = " + str(sum(probaLength)))
#print("sum(probaStart) = " + str(sum(probaStart.values())))

#for alpha in bigrams.keys():
#    print("sum(bigrams["+alpha+"]) =" + str(sum(bigrams[alpha].values())))

exit = False
while not exit:
    length = 1
    rLength = random.random()
    for p in probaLength:
        if rLength > p:
            rLength -= p
            length += 1
        else:
            break

    word = ""
    rFirst = random.random()
    for alpha in probaStart.keys():
        if rFirst > probaStart[alpha]:
            rFirst -= probaStart[alpha]
        else:
            word = alpha
            break

    for i in range(1, length):
        rNext = random.random()
        alpha = word[-1]
        for beta in bigrams[alpha].keys():
            if rNext > bigrams[alpha][beta]:
                rNext -= bigrams[alpha][beta]
            else:
                word += beta
                break

    print(word)

    retry = input("Do you want to retry ? (Y|N) :")
    exit =  (list(retry[0]) == "N")
    print("")
