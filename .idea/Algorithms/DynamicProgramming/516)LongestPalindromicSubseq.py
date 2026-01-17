class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0;
        n = len(s)
        dp = [[0 for high in range(len(s)+1)] for low in range(len(s))]
        for low in range(n-1, -1, -1):
            dp[low][low+1] = 1;
            for high in range(low+2, n+1):
                if s[low] == s[high-1]:
                    dp[low][high] = 2 + dp[low+1][high-1]
                else:
                    dp[low][high] = max(dp[low+1][high], dp[low][high-1])
        return dp[0][len(s)]



sol = Solution()
print(sol.longestPalindromeSubseq("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"))
