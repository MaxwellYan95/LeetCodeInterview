class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        minList = {}
        def minRecur(word1: str, word2: str) -> int:
            combo = word1 + " " + word2;
            if len(minList) != 0:
                if combo in minList:
                    return minList[combo];

            if word1 == "" and word2 == "":
                minList[combo] = 0;
                return 0;
            if word1 == "":
                minList[combo] = len(word2);
                return len(word2);
            if word2 == "":
                minList[combo] = len(word1);
                return len(word1);
            if (word1[0] == word2[0]):
                return minRecur(word1[1:], word2[1:]);
            insert = 1 + minRecur(word1, word2[1:]);
            delete = 1 + minRecur(word1[1:], word2);
            replace = 1 + minRecur(word1[1:], word2[1:]);
            minList[combo] = min(insert, delete, replace);
            return min(insert, delete, replace);
        return minRecur(word1, word2);

sol = Solution();
print(sol.minDistance("horse", "ros"));
