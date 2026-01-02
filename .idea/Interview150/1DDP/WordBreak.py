class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sortedWord = sorted(wordDict, key=len, reverse=True);
        return self.iteration(s, sortedWord);
    def iteration(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True;
        if len(wordDict[len(wordDict)-1]) > len(s):
            return False;
        for word in wordDict:
            isLength = (len(word) <= len(s));
            if s[0: len(word)] == word and isLength:
                iter = self.iteration(s[len(word):], wordDict);
                if iter == True:
                    return True;
        return False;

sol = Solution();
sol.wordBreak("leetcode", ["leet", "code"]);

