from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        def isPunctOrSpace(w: str):
            if list(punct).count(w) > 0 or w == ' ':
                return True
            return False

        beg = 0;
        end = 1;
        punct = "!?',;.";
        wordDict = defaultdict(int)
        paragraph += " "
        while end < len(paragraph):
            endChar = paragraph[end]
            if isPunctOrSpace(endChar):
                word = paragraph[beg:end].lower()
                if banned.count(word) == 0:
                    wordDict[word] += 1
                beg = end+1;
                end = end+1;
                while end < len(paragraph) and isPunctOrSpace(paragraph[beg]):
                    beg = beg+1;
                    end = end+1;
            end = end + 1;
        maximum = 0;
        maxWord = "";
        for word in wordDict.keys():
            if maximum <= wordDict[word]:
                maximum = wordDict[word];
                maxWord = word;
        return maxWord



sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

