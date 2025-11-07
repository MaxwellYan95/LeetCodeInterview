from collections import defaultdict
from collections import deque;

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0;
        tempList = wordList.copy();
        tempList.append(beginWord)
        visited = set();
        myStack = deque();
        numPath = 1;
        myStack.append(beginWord);
        visited.add(beginWord);
        while len(myStack) != 0:
            for _ in range(len(myStack)):
                latest = myStack.popleft();
                if latest == endWord:
                    return numPath;
                for word in wordList:
                    if word not in visited and self.canTransform(word, latest):
                        visited.add(word);
                        myStack.append(word);
            numPath += 1;
        return 0;

    def canTransform(self, begin: str, end: str):
        changes = 0;
        for i in range(len(begin)):
            if begin[i] != end[i]:
                changes = changes + 1;
        return changes == 1;

sol = Solution();
print(sol.ladderLength("hit", "cog", ["hot","cog","dot","dog","hit","lot","log"]));