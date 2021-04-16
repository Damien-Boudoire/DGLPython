import string
import random

ALPHABET = list(string.ascii_lowercase)

def generateListRandString(listLength, strLength):
    randStrings = []
    for i in range(0, listLength):
        str = ""
        for j in range(0, strLength):
            str += ALPHABET[random.randint(0, 25)]
        randStrings.append(str)
    return randStrings

def compareRank(a,b):
    if a == b:
        return 0
    for character in ALPHABET:
        if a == character:
            return -1
        if b == character:
            return 1



def increaseWordRankOld(inWord):
    listWord = list(inWord)
    changeOn = -1
    for i in range(len(listWord)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if compareRank(listWord[j], listWord[i]) > 0:
                char = listWord[i]
                listWord[i] = listWord[j]
                listWord[j] = char
                changeOn = j
                break
        if changeOn >= 0:
            break
    outWord = "".join(listWord[0:changeOn+1]+sorted(listWord[changeOn+1:]))
    return outWord

def increaseWordRank(inWord):
    listWord = list(inWord)

    for i in range(len(listWord) - 1, -1, -1):
        prefix = listWord[:i]
        current = listWord[i]
        suffix = sorted(listWord[i+1:])
        for j in range(0, len(suffix)):
            if compareRank(listWord[i], suffix[j]) < 0:
                return "".join(prefix + [suffix[j]] + suffix[:j] + [current]  +suffix[j+1:])

def test():
    wordList = generateListRandString(10,5)
    for word in wordList:
        print(word)
        print(increaseWordRank(word))
        print("-----")

#test()
inWord = list(input("Veuillez renseigner un mot et un seul,"
                    " sans espace ni aucun autre caractère"
                    " que les 26 lettres de l’alphabet (sans accent ni majuscule)."))
print(increaseWordRank(inWord))