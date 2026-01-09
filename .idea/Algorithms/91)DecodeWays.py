from collections import defaultdict

class Solution:

    mapping = defaultdict(int)

    def numDecodings(self, s: str) -> int:
        if len(s) <= 2:
            ways = self.twoDigits(s);
            self.mapping[s] = ways;
            return ways
        middle = len(s)//2;
        leftNum = self.numDecodings(s[:middle])
        rightNum = self.numDecodings(s[middle:])
        middleNum = s[middle-1: middle+1]
        multi = self.twoDigits(middleNum)
        result = 0;
        if multi == 2:
            result = self.mapping[s[:middle-1]] * self.mapping[s[middle+1:]]
            + leftNum * rightNum
        else:
            result = leftNum * rightNum
        self.mapping[s] = result;
        return result;

    def twoDigits(self, s: str):
        number = int(s);
        if number <= 26:
            if number < 10:
                return 1;
            else:
                return 2;
        else:
            return 1;

sol = Solution()
print(sol.numDecodings("226"))