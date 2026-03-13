import dictionary as d

class Translator:

    def __init__(self):
        self.dict = d.Dictionary()


    def printMenu(self):
        print("Translator Alien-Italian")
        print("-"*40)
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")
        print("-" * 40)

    def loadDictionary(self, filename):
        with open(filename) as f:
            for line in f:
                parti = line.strip().split(" ")
                self.dict.addWord(parti[0], parti[1])

    def handleAdd(self, entry):
        parti = entry.strip().split()
        aliena = parti[0]
        for traduzione in parti[1:]:
            self.dict.addWord(aliena, traduzione)

    def handleTranslate(self, query):
        risultato = self.dict.translate(query)
        if risultato is not None:
            return risultato
        else:
            return "Traduzione non trovata"

    def handleWildCard(self, query):
        risultati = self.dict.translateWordWildCard(query)
        if len(risultati) == 0:
            print("Nessuna parola trovata!")
        else:
            for r in risultati:
                print(r)

if __name__ == "__main__":
    t = Translator()
    t.loadDictionary("dictionary.txt")
    print(t.dict.dizionario_parole)