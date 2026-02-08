class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lowLen = min(len(word2), len(word1))
        result = ""
        for index in range(lowLen):
            result += str(word1[index])
            result += str(word2[index])
        if len(word2) > len(word1):
            result += word2[lowLen:]
        else:
            result += word1[lowLen:]
        return result