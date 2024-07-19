"""
Uppgift
Skriv ett program som läser en mening bestående av minst två ord. 
Programmet ska sedan skriva ut ett meddelande 
där det talar om hur många ord användaren skrev in 
och vilket som det första och det sista ordet. 

Planering
För att hantera felaktik input måste inputen vara i en while-loop.
Det behövs valideringskod som ska kolla om inputen är korrekt varje gång användaren skriver in något.



Ta emot input -> Trimma bort whitespace runtom -> Validera för att se om det är minst två ord, 
om inte så upprepa loop med input -> Vid korrekt input, dela upp meningen till en lista med orden
-> Skriv ut antalet ord, första och sista ordet.
"""

isCorrectSentence = False


def validateInput(inputString):
    if len(inputString) < 1:
        print("Du måste skriva något.")
        return False

    elif len(inputString.split()) < 2:
        print("Du måste skriva minst två ord.")
        return False

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
