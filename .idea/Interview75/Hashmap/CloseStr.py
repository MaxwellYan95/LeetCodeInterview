from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = defaultdict(int);
        dict2 = defaultdict(int);
        allLetters = set()
        if len(word1) != len(word2):
            return False;
        for index in range(len(word1)):
            dict1[word1[index]] += 1
            dict2[word2[index]] += 1
            allLetters.add(word1[index])
            allLetters.add(word2[index])
        if set(dict1.keys()) != set(dict2.keys()):
            return False;
        nums1 = [];
        nums2 = [];
        for letter in allLetters:
            nums1.append(dict1[letter]);
            nums2.append(dict2[letter]);
        nums1.sort()
        nums2.sort()
        for index in range(len(nums2)):
            if nums1[index] != nums2[index]:
                return False;
        return True;

sol = Solution()
print(sol.closeStrings("uau", "ssx"))
