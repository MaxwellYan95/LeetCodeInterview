import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        steps = 0;
        if endWord not in wordList:
            return steps;
        stack = collections.deque();
        stack.append(beginWord);
        wordList = set(wordList);
        visited = [];
        while stack:
            for _ in range(len(stack)):
                word = stack.popleft();
                if word == endWord:
                    return steps + 1;
                if word in wordList:
                    wordList.remove(word);
                for w in wordList:
                    if self.canTransform(w, word) and w not in visited:
                        stack.append(w);
                        visited.append(w);
            steps += 1;
        return 0;

    def canTransform(self, word1: str, word2: str):
        changes = 0;
        for index in range(len(word1)):
            if word2[index] != word1[index]:
                changes += 1;
        return changes == 1;

sol = Solution();
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]));
print(sol.ladderLength("hot", "dog", ["hot","dog"]));
print(sol.ladderLength("a", "c", ["a","b", "c"]));
