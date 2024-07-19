"""
Uppgift
Skriv ett program som läser en mening bestående av minst två ord. 
Programmet ska sedan skriva ut ett meddelande 
där det talar om hur många ord användaren skrev in 
och vilket som det första och det sista ordet. 

Planering
input -> trimma bort whitespace runtom -> validering för att se om det är minst två ord, 
om inte så upprepa loop med input, annars analysera mening -> dela upp meningen till ord i lista 
-> output med första, sista och antalet ord.


"""

isCorrectSentence = False


def validateInput(inputString):
    if len(inputString) < 1:
        print("Du måste skriva något.")
        print("check 1")
        return False

    elif len(inputString.split()) < 2:
        print("check 2")
        print("Du måste skriva minst två ord.")
        return False

    print("check 3")
    words = inputString.split()
    for word in words:
        if not any(char.isalpha() for char in word):
            print("'{}' är inte ett giltigt ord.".format(word))
            return False

    return True


while isCorrectSentence is False:
    sentence = input("Skriv några ord, minst två: ")
    isCorrectSentence = validateInput(sentence)

sentence = sentence.strip()
list = sentence.split()
print("Du skrev " + str(len(list)) + " ord.")
print("Första ordet är " + list[0] + ".")
print("Sista ordet du skrev är " + list[-1] + ".")
