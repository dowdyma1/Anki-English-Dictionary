from PyDictionary import PyDictionary
import pyperclip


def main():
    dictionary = PyDictionary()
    userInput = ""
    definition = ""

    print("type -1 to quit.")
    while(userInput != "-1"):
        userInput = input("Type word to lookup: ")
        if(userInput == "-1"):
            break

        word = userInput
        querry = dictionary.meaning(word)
        word  = word.capitalize()
        try:
            querry.items()
        except:
            print("Could not find {} in dictionary.".format(word))

        definition += word + "\n\n"
        for key, value in querry.items():
            definition += key + ":\n"
            for i in range(len(value)):
                definition += str(i+1) + ". " + value[i] + "\n"
            definition += "\n"

        pyperclip.copy(definition)
        print("Definition copied to clipboard.")

        definition = ""


if __name__ == "__main__":
    main()
