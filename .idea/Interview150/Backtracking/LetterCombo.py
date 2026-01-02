class Solution:
    dictMap = {'2': ["a", "b", "c"],
               '3': ["d", "e", "f"],
               '4': ["g", "h", "i"],
               '5': ["j", "k", "l"],
               '6': ["m", "n", "o"],
               '7': ["p", "q", "r", "s"],
               '8': ["t", "u", "v"],
               '9': ["w", "x", "y", "z"]};
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return [];
        digitLst = list(digits);
        if (len(digitLst) == 1):
            return self.dictMap[digitLst[0]];
        else:
            result = [];
            lst = self.letterCombinations("".join(digitLst[1:]));
            letters = self.dictMap[digitLst[0]];
            for element in lst:
                for l in letters:
                    result.append(str(l) + str(element));
            return result;

sol = Solution();
print(sol.letterCombinations("23"));