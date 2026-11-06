from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        def fixWord(word: str):
            punct = "!?',;."
            w = word;
            if list(punct).count(w[0]) > 0:
                w = w[1:]
            if list(punct).count(w[len(w)-1]) > 0:
                w = w[:len(w)-1]
            return w.lower();

        wordLst = paragraph.split(" ")
        punct = "!?',;."
        wordDict = defaultdict(int)
        for word in wordLst:
            word = fixWord(word)
            if banned.count(word) > 0:
                continue;
            wordDict[word] += 1;

        maximum = 0;
        maxWord = ""
        for word in wordDict.keys():
            if maximum <= wordDict[word]:
                maximum = wordDict[word];
                maxWord = word;
        return maxWord

sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

