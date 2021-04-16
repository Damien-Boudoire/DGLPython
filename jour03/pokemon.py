import re

pokedex = open("Pokedex.csv","r")

pokemonNames = []

exit = False
line = pokedex.readline()
while not exit:
    line = pokedex.readline()
    if len(line) == 0:
        exit = (len(line) == 0)
        continue
    elements = re.split(",", line)
    pokemonNames.append(elements[2])

pokedex.close()

data = open("data.txt", "r")
txt = data.read()

pokelatin = ""
for pokemon in pokemonNames:
    match = re.search(str(pokemon), txt)
    if match is not None:
        pokelatin = pokemon

print(pokelatin)