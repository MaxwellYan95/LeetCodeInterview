class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dictWord = {};
        for word in strs:
            newKey = "".join(sorted(list(word)));
            if newKey not in dictWord:
                dictWord[newKey] = [word];
            else:
                dictWord[newKey].append(word);
        return list(dictWord.values());

sol = Solution();
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]));