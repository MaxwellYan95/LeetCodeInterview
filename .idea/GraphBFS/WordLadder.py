from collections import defaultdict
from collections import deque;

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0;
        tempList = wordList.copy();
        tempList.append(beginWord)
        transDict = self.createDict(set(tempList));
        visited = set();
        myStack = deque();
        numPath = 1;
        myStack.append(beginWord);
        visited.add(beginWord);
        while len(myStack) != 0:
            latest = myStack.pop();
            if latest == endWord:
                return numPath;
            neighbors = transDict[latest];
            for neigh in neighbors:
                if neigh not in visited:
                    visited.add(neigh);
                    myStack.append(neigh);
            numPath += 1;

        return 0;

    def createDict(self, wordList: list[str]):
        dictionary = defaultdict(list)
        for word1 in wordList:
            for word2 in wordList:
                if self.canTransform(word1, word2):
                    dictionary[word1].append(word2);
        return dictionary;

    def canTransform(self, begin: str, end: str):
        changes = 0;
        for i in range(len(begin)):
            if begin[i] != end[i]:
                changes = changes + 1;
        return changes == 1;

sol = Solution();
print(sol.ladderLength("hit", "cog", ["hot","cog","dot","dog","hit","lot","log"]));