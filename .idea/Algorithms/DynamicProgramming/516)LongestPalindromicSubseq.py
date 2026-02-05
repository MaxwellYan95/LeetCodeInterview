class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1 for i in range(len(s)+1)] for j in range(len(s))]
        for index in range(len(s)):
            dp[index][index+1] = 1;
            dp[index][index] = 0;
        for low in range(len(s)-1, -1, -1):
            for high in range(low+1, len(s)+1):
                if dp[low][high] == -1:
                    result = 0;
                    if s[low] == s[high-1]:
                        result = dp[low+1][high-1] + 2;
                    else:
                        result = max(dp[low][high-1], dp[low+1][high])
                    dp[low][high] = result;
        return dp[0][len(s)];




sol = Solution()
print(sol.longestPalindromeSubseq("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"))
