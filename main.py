from PyDictionary import PyDictionary

dictionary = PyDictionary()

x = ["Abhorrence", "Exultation", "Sinewy", "Adherent", "Self-aggrandizing", "Sibilant", "Propriety", "Relish", "Calamity", "Jaunt", "Multifarious", "Sedition", "modicum", "covetous", "Oblong", "Reticence", "Surfeit", "Malevolent", "Isometric", "Yearning", "Dissent", "Vindicated", "Derelict", "Exhortation", "Surly", "vestibule", "Assuage", "Precipitous", "Menace", "Taciturn", "Supplication", "Tenuous", "Abashed", "Numinosity"]

error = []
for word in x:
    querry = dictionary.meaning(word)
    word  = word.capitalize()
    try:
        querry.items()
    except:
        error.append(word)
        break

    print(word)
    for key, value in querry.items():
        print(key + ":")
        for i in range(len(value)):
            print(str(i+1) + ". " + value[i])
        print()
    print()

print("Errors:")
print(error)
