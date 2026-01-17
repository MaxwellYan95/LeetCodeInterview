class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0;
        dp = [["" for high in range(len(s)+1)] for low in range(len(s))]
        dpLen = [[-1 for high in range(len(s)+1)] for low in range(len(s))]
        for index in range(len(s)):
            dp[index][index+1] = s[index];
            dpLen[index][index+1] = 1;
            dpLen[index][index] = 0;
        def recur(low: int, high: int) -> str:
            if dpLen[low][high] != -1:
                return dp[low][high]
            maxLen = 0;
            maxStr = "";
            for index in range(low, high):
                length = 0;
                string = "";
                leftRecur = recur(low, index);
                rightRecur = recur(index, high);
                middle = s[index];
                if leftRecur == rightRecur:
                    string = leftRecur + "" + middle + "" + rightRecur;
                elif len(leftRecur) > len(rightRecur):
                    string = leftRecur;
                else:
                    string = rightRecur;
                length = len(string)
                if length > maxLen:
                    maxLen = length;
                    maxStr = string;
            dpLen[low][high] = maxLen;
            dp[low][high] = maxStr;
            return maxStr;
        return len(recur(0, len(s)))


sol = Solution()
print(sol.longestPalindromeSubseq("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"))
