class WordDictionary:

    def __init__(self):
        self.lst = [];

    def addWord(self, word: str) -> None:
        if word not in self.lst:
            self.lst.append(word);

    def search(self, word: str) -> bool:
        if word in self.lst:
            return True;
        if '.' in list(word):
            return self.dotMatch(word);
        return False;

    def dotMatch(self, word: str) -> bool:
        foundWord = False;
        for element in self.lst:
            if foundWord == True:
                return True;
            else:
                foundWord = True;
            if len(element) == len(word):
                elemLst = list(element);
                wordLst = list(word);
                for index in range(len(elemLst)):
                    if wordLst[index] != '.' and elemLst[index] != wordLst[index]:
                        foundWord = False;
                        break;
            else:
                foundWord = False;
        return foundWord;