class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s2) == 0:
            if s1 == s3:
                return True;
            return False;
        elif len(s1) == 0:
            if s2 == s3:
                return True;
            return False;
        if (s1[0] == s3[0]) and (s2[0] == s3[0]):
            return self.isS1Interleave(s1[1:], s2, s3[1:]) or self.isS1Interleave(s2[1:], s1, s3[1:]);
        elif s1[0] == s3[0]:
            return self.isS1Interleave(s1[1:], s2, s3[1:]);
        elif s2[0] == s3[0]:
            return self.isS1Interleave(s2[1:], s1, s3[1:]);
        return False;

    def isS1Interleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s2) == 0:
            if s1 == s3:
                return True;
            return False;
        elif len(s1) == 0:
            if s2 == s3:
                return True;
            return False;
        else:
            if (s1[0] == s3[0]) and (s2[0] == s3[0]):
                return self.isS1Interleave(s1[1:], s2, s3[1:]) or self.isS1Interleave(s1, s2[1:], s3[1:]);
            elif s1[0] == s3[0]:
                return self.isS1Interleave(s1[1:], s2, s3[1:]);
            elif s2[0] == s3[0]:
                return self.isS1Interleave(s1, s2[1:], s3[1:]);
            else:
                return False;

sol = Solution();
sol.isInterleave("a", "b", "ab");



