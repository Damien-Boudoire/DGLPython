text = input("Veuillez entrer une ligne de texte : ")

file = open("output.txt", "w")
file.write(text)

file.close()