from collections import defaultdict

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if len(words) == 1:
            return list(words[0])
        dictList = [defaultdict(int) for w in words]
        combo = ""
        for w in words:
            combo += w + ""
        allLetters = set(list(combo));
        for index in range(len(words)):
            w = words[index];
            for char in w:
                dictList[index][char] += 1;

        result = []
        for letter in allLetters:
            num = float('inf');
            same = True;
            for index in range(len(words)):
                num = min(num, dictList[index][letter]);
            result.extend(num * [letter])

        return result

sol = Solution()
print(sol.commonChars(["bella","label","roller"]))
