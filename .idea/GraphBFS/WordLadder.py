class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0;
        if len(wordList) == 1:
            if endWord == wordList[0] and self.canTransform(beginWord, endWord) == True:
                return 1;
            return 0;
        numbers = [];
        trans = [];
        for word in wordList:
            if self.canTransform(beginWord, word) == True:
                if word == beginWord:
                    continue;
                if word == endWord:
                    return 2;
                trans.append(word);
        wordCopy = wordList.copy();
        wordCopy.remove(trans);
        for move in trans:
            next = self.ladderLength(move, endWord, wordCopy);
            if next != 0:
                numbers.append(next + 1);
        if len(numbers) == 0:
            return 0;
        return min(numbers);

    def canTransform(self, first: str, second: str):
        firstList = list(first);
        secondList = list(second);
        changes = 0;
        for index in range(len(firstList)):
            if firstList[index] != secondList[index]:
                changes = changes + 1;
        return changes < 2;

sol = Solution();
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]));
print(sol.ladderLength("hot", "dog", ["hot","dog"]));
print(sol.ladderLength("a", "c", ["a","b", "c"]));
