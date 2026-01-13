class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        dpMax = [[-1 for i in range(len(nums)+1)] for j in range(len(nums))];
        dpMin = [[-1 for i in range(len(nums)+1)] for j in range(len(nums))];
        dpStr = [["" for i in range(len(nums)+1)] for j in range(len(nums))];
        for i in range(len(nums)):
            dpMax[i][i+1] = nums[i];
            dpMin[i][i+1] = nums[i];
            dpStr[i][i+1] = str(nums[i]);
        for i in range(len(nums)-1):
            dpMax[i][i+2] = float(nums[i]/nums[i+1]);
            dpMin[i][i+2] = float(nums[i]/nums[i+1]);
            dpStr[i][i+2] = "" + str(nums[i]) + "/" + str(nums[i+1]);
        def recur(lower: int, higher: int) -> str:
            curNum = 0;
            curStr = "";
            if dpMax[lower][higher] != -1:
                return dpStr[lower][higher]
            for i in range(lower+1, higher):
                leftStr = recur(lower, i);
                rightStr = recur(i, higher);
                leftNum = dpMax[lower][i]
                rightNum = dpMax[i][higher]
                if curNum < float(leftNum / rightNum):
                    curNum = float(leftNum / rightNum);
                    if leftStr[0] == '(':
                        leftStr = leftStr[1:len(leftNum)-1]
                    if rightStr != '':
                        curStr = leftStr + '/(' + rightStr + ')'
                    else:
                        curStr = leftStr + '/' + rightStr

            allNum = float(nums[lower])
            allStr = str(nums[lower])
            for i in range(lower+1, higher):
                allNum /= nums[i];
                allStr += ("/" + str(nums));
            if curNum < allNum:
                curNum = allNum;
                curStr = allStr;

            dpMax[lower][higher] = curNum;
            dpStr[lower][higher] = curStr;
            return curStr;
        return recur(0, len(nums))

sol = Solution();
print(sol.optimalDivision([1000,100,10,2]))