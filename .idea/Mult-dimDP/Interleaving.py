class Solution:
    class Solution:
        def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
            def recurInterleave(s1: str, s2: str, s3: str) -> bool:
                if (len(s1) == 0):
                    return s3 == s2;
                elif (len(s2) == 0):
                    return s3 == s1;
                elif (s1[0] == s3[0] and s2[0] == s1[0]):
                    return recurInterleave(s1[1:], s2, s3[1:]) or recurInterleave(s1, s2[1:], s3[1:]);
                elif (s1[0] == s3[0]):
                    return recurInterleave(s1[1:], s2, s3[1:]);
                elif (s2[0] == s3[0]):
                    return recurInterleave(s1, s2[1:], s3[1:]);
                else:
                    return False;
            return recurInterleave(s1, s2, s3);
sol = Solution();
print(sol.isInterleave("a", "b", "a"));



