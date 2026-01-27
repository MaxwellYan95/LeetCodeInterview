class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) <= 1:
            return 0;
        n = len(s)
        dpL = [-1 for i in range(n)]
        dpR = [-1 for i in range(n)]
        if s[0] == 'L':
            dpL[0] = 1;
            dpR[0] = 0;
        else:
            dpL[0] = 0;
            dpR[0] = 1;
        count = 0;
        for index in range(1, n):
            if s[index] == 'L':
                dpL[index] = dpL[index-1]+1;
                dpR[index] = dpR[index-1];
            else:
                dpL[index] = dpL[index-1];
                dpR[index] = dpR[index-1]+1;
            if dpL[index] == dpR[index]:
                count += 1;
        return count
