class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sLst = list(s)
        tLst = list(t)
        mapping = {}
        for i in range(len(s)):
            curS = sLst[i];
            curT = tLst[i];
            if curS in mapping:
                if mapping[curS] != curT:
                    return False;
            mapping[curS] = curT;
        mapping = {}
        for i in range(len(s)):
            curS = sLst[i];
            curT = tLst[i];
            if curT in mapping:
                if mapping[curT] != curS:
                    return False;
            mapping[curT] = curS;
        return True;




sol = Solution()
print(sol.isIsomorphic("badc", "baba"))
print(sol.isIsomorphic("paper", "title"))



    