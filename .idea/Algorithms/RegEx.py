class Solution:
    # def isMatch(self, s: str, p: str) -> bool:


    # Examples
    # 1. Changes .*.. to ...*
    # 2. Changes **. to .*
    def simplifyEx(self, p: str) -> str:
        newP = "";
        lstP = list(p);
        index = 0;
        while index < len(lstP):
            curP = lstP[index];
            periods = 0;
            hasStar = False;
            if self.isReg(curP):
                while (self.isReg(curP) and index < len(lstP)):
                    if self.isPeriod(curP):
                        periods += 1;
                    elif self.isStar(curP):
                        hasStar = True;
                    index += 1;
                    curP = lstP[min(index, len(lstP)-1)];
                for p in range(periods):
                    newP += (".");
                if hasStar:
                    newP += ("*")
            else:
                newP += (curP + "")
                index += 1;
        return newP;

    def isStar(self, p: str) -> bool:
        return p == '*';

    def isPeriod(self, p: str) -> bool:
        return p == '.';

    def isReg(self, p: str) -> bool:
        return self.isStar(p) or self.isPeriod(p);

sol = Solution();
print(sol.simplifyEx("*.**..aaa..***.*..*"))
