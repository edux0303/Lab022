import translator as tr
import dictionary as dr


t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()
    txtIn = input()

    if int(txtIn) == 1:
        txtIn = input("Ok, quale parola devo aggiungere?")
        t.handleAdd(txtIn)

    elif int(txtIn) == 2:
        txtIn = input("Ok, quale parola devo cercare? ")
        print(t.handleTranslate(txtIn.strip()))

    elif int(txtIn) == 3:
        txtIn = input("Ok, quale parola devo cercare? ")
        t.handleWildCard(txtIn.strip())


    elif int(txtIn) == 4:
        t.dict.stampaDizionario()
        break
    elif int(txtIn) == 5:
        break