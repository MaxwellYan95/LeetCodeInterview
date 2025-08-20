class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomSet = sorted(set(list(ransomNote)));
        ransomDict = {letter: list(ransomNote).count(letter) for letter in ransomSet}
        magSet = sorted(set(list(magazine)));
        magDict = {letter: list(magazine).count(letter) for letter in magSet}
        if len(ransomSet) > len(magSet):
            return False
        for key in ransomSet:
            contain = key in magSet;
            if contain == False:
                return False;
            else:
                magCount = magDict.get(key);
                ransomCount = ransomDict.get(key);
                if (magCount < ransomCount):
                    return False;
        return True;


