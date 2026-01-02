class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternDict = {}
        wordLst = s.split(" ");
        patternLst = list(pattern);
        if len(wordLst) != len(patternLst):
            return False;
        for index in range(len(wordLst)):
            w = wordLst[index];
            p = patternLst[index];
            if p not in patternDict.keys():
                if w in patternDict.values():
                    return False;
                patternDict[p] = w;
            elif patternDict[p] != w:
                return False;
        return True;
sol = Solution();
print(sol.wordPattern("abba", "dog cat cat dog"))
