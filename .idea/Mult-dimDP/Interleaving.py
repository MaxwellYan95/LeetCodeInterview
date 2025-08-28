class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s3)+1)]
        def recurInterleave(s1: str, s2: str, s3: str) -> bool:
            if (dp[len(s3)][len(s2)] == True):
                return True;
            elif (len(s1) == 0):
                dp[len(s3)][len(s2)] = (s3 == s2);
                return s3 == s2;
            elif (len(s2) == 0):
                dp[len(s3)][len(s2)] = (s3 == s1);
                return s3 == s1;
            elif (len(s1) == 0):
                dp[len(s3)][len(s2)] = (s3 == s2);
                return s3 == s2;
            elif (s1[0] == s3[0] and s2[0] == s1[0]):
                dp[len(s3)][len(s2)] = (recurInterleave(s1[1:], s2, s3[1:]) or recurInterleave(s1, s2[1:], s3[1:]));
                return dp[len(s3)][len(s2)];
            elif (s1[0] == s3[0]):
                dp[len(s3)][len(s2)] = recurInterleave(s1[1:], s2, s3[1:]);
                return dp[len(s3)][len(s2)];
            elif (s2[0] == s3[0]):
                dp[len(s3)][len(s2)] = recurInterleave(s1, s2[1:], s3[1:]);
                return dp[len(s3)][len(s2)];
            else:
                dp[len(s3)][len(s2)] = False;
            return False;
        return recurInterleave(s1, s2, s3);
sol = Solution();
print(sol.isInterleave("a", "b", "a"));



