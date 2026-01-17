class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0;
        dp = {}
        dp[""] = 0;
        for index in range(len(s)):
            dp[s[index]] = 1;
        def recur(subStr: str):
            result = 0;
            if subStr in dp:
                return dp[subStr];
            elif self.isPalindrone(subStr):
                result = len(subStr)
            else:
                for index in range(len(subStr)):
                    result = max(result, recur(subStr[:index] + "" + subStr[index+1:]))
            dp[subStr] = result;
            return result;
        return recur(s)

    def isPalindrone(self, s: str) -> bool:
        low = 0;
        high = len(s)-1
        while low < high:
            if s[low] != s[high]:
                return False;
            low += 1;
            high -= 1;
        return True;

sol = Solution()
print(sol.longestPalindromeSubseq("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"))
