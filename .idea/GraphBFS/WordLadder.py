import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        moves = 0;
        stack = collections.deque([beginWord]);
        visited = [];
        if endWord not in wordList:
            return 0;
        while stack:
            for _ in range(len(stack)):
                word = stack.popleft();
                visited.append(word);
                if word in wordList:
                    wordList.remove(word);
                if word == endWord:
                    return moves + 1;
                adjacent = []
                for w in wordList:
                    if self.canTransform(w, word) and w not in visited:
                        stack.append(w);
                        adjacent.append(w);
                for adj in adjacent:
                    wordList.remove(adj);
            moves += 1;
        return 0;


    def canTransform(self, first: str, second: str):
        firstList = list(first);
        secondList = list(second);
        changes = 0;
        for index in range(len(firstList)):
            if firstList[index] != secondList[index]:
                changes = changes + 1;
        return changes == 1;

sol = Solution();
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]));
print(sol.ladderLength("hot", "dog", ["hot","dog"]));
print(sol.ladderLength("a", "c", ["a","b", "c"]));
