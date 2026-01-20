class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        self.numMap = {};
        self.maxMap = {};
        for s in strs:
            ones = 0;
            zeroes = 0;
            for char in s:
                if char == '1':
                    ones += 1;
                else:
                    zeroes += 1;
            self.numMap[s] = [ones, zeroes];
            if ones <= n and zeroes <= m:
                self.maxMap[s] = 1;
            else:
                self.maxMap[s] = 0;
        def recur(strLst: list[str]):
            comboStr = "";
            one = 0;
            zero = 0;
            for s in strLst:
                one += self.numMap[s][0];
                zero += self.numMap[s][1];
                comboStr += (s + "");
            self.numMap[comboStr] = [one, zero];
            if comboStr in self.maxMap:
                return self.maxMap[comboStr];
            if one <= n and zero <= m:
                self.maxMap[comboStr] = len(strLst);
                return self.maxMap[comboStr];
            result = 0;
            for index in range(len(strLst)):
                result = max(result, recur(strLst[:index] + strLst[index+1:]));
            return result;
        return recur(strs);

sol = Solution()
res = sol.findMaxForm(["10","0001","111001","1","0"], 5, 3)
print()

