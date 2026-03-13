class Dictionary:


    def __init__(self):
        self.dizionario_parole = {}
        pass

    def addWord(self, alien, translation):
        if alien in self.dizionario_parole.keys():
            self.dizionario_parole[alien].append(translation)
        else: self.dizionario_parole[alien] = [translation]



    def translate(self, query):
        return self.dizionario_parole.get(query, None)

    def translateWordWildCard(self, query):
        risultati = []
        for key in self.dizionario_parole.keys():
            if len(key) != len(query):
                continue
            match = True
            for c_key, c_query in zip(key, query):
                if c_query != '?' and c_key != c_query:
                    match = False
                    break
            if match:
                risultati.append(self.dizionario_parole[key])
        return risultati


    def stampaDizionario(self):
        for(key, val) in self.dizionario_parole.items():
            print(key, val)

if __name__ == "__main__":
    dic = Dictionary()
    dic.addWord("kissa", "gatto")
    dic.addWord("kissa", "cat")
    print(dic.translate("kissa"))


