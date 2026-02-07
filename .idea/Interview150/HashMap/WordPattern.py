class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordDict = {}
        letterDict = {}
        letterLst = list(pattern)
        wordLst = s.split(" ")
        if len(wordLst) != len(letterLst):
            return False
        for i in range(len(letterLst)):
            letter = letterLst[i]
            word = wordLst[i]
            if word in wordDict:
                if wordDict[word] != letter:
                    return False;
            if letter in letterDict:
                if letterDict[letter] != word:
                    return False;
            letterDict[letter] = word;
            wordDict[word] = letter;
        return True



sol = Solution();
print(sol.wordPattern("abba", "dog cat cat dog"))
