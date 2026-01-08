from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        allLetters = set(list(ransomNote))
        ransonDict = defaultdict(int)
        magDict = defaultdict(int)
        for letter in list(ransomNote):
            ransonDict[letter] += 1;
        for letter in list(magazine):
            magDict[letter] += 1;
        for letter in allLetters:
            if ransonDict[letter] > magDict[letter]:
                return False;
        return True;


