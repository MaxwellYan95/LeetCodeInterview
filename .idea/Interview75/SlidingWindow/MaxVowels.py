class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        subS = s[:k]
        dp = [0]
        result = 0;
        vowels = "aeiou"
        for s1 in subS:
            if s1 in vowels:
                dp[0] += 1
        print("0 : " + str(dp[0]))
        result = dp[0];
        print(len(s));
        for index in range(1, len(s)-k+1):
            if result == k:
                return result;
            dp.append(dp[index-1])
            if s[index-1] in vowels:
                dp[index] -= 1;
            print(s[index+k-1])
            if s[index+k-1] in vowels:
                dp[index] += 1;
            result = max(result, dp[index]);
            print(str(index) + " : " + str(dp[index]))
        return result

sol = Solution();
print(sol.maxVowels("abciiidef", 3))