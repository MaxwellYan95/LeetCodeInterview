class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        dpMax = [[-1 for i in range(len(nums)+1)] for j in range(len(nums))];
        dpMin = [[-1 for i in range(len(nums)+1)] for j in range(len(nums))];
        dpMaxStr = [["" for i in range(len(nums)+1)] for j in range(len(nums))];
        dpMinStr = [["" for i in range(len(nums)+1)] for j in range(len(nums))];

        for i in range(len(nums)):
            dpMax[i][i+1] = nums[i];
            dpMin[i][i+1] = nums[i];
            dpMaxStr[i][i+1] = str(nums[i]);
            dpMinStr[i][i+1] = str(nums[i]);
        for i in range(len(nums)-1):
            dpMax[i][i+2] = float(nums[i]/nums[i+1]);
            dpMin[i][i+2] = float(nums[i]/nums[i+1]);
            dpMaxStr[i][i+2] = "" + str(nums[i]) + "/" + str(nums[i+1]);
            dpMinStr[i][i+2] = "" + str(nums[i]) + "/" + str(nums[i+1]);

        def formatString(leftStr: str, rightStr: str) -> str:
            if leftStr[0] == '(':
                leftStr = leftStr[1:len(leftStr)-1]
            if rightStr != '':
                return leftStr + '/(' + rightStr + ')'
            else:
                return leftStr + '/' + rightStr

        def recur(lower: int, higher: int):
            maxNum = 0;
            minNum = 0;
            maxStr = "";
            minStr = "";

            if dpMax[lower][higher] != -1:
                return
            for i in range(lower+1, higher):
                recur(lower, i);
                recur(i, higher);
                leftMax = dpMax[lower][i]
                rightMax = dpMax[i][higher]
                leftMin = dpMin[lower][i]
                rightMin = dpMin[i][higher]
                leftMaxStr = dpMaxStr[lower][i]
                rightMaxStr = dpMaxStr[i][higher]
                leftMinStr = dpMinStr[lower][i]
                rightMinStr = dpMinStr[i][higher]
                if minNum > float(leftMin / rightMax):
                    minNum = float(leftMin / rightMax)
                    minStr = formatString(leftMinStr, rightMaxStr)
                if maxNum < float(leftMax / rightMin):
                    maxNum = float(leftMax / rightMin);
                    maxStr = formatString(leftMaxStr, rightMinStr)
            allNum = float(nums[lower])
            allStr = str(nums[lower])
            for i in range(lower+1, higher):
                allNum /= nums[i];
                allStr += ("/" + str(nums));
            if maxNum < allNum:
                maxNum = allNum;
                maxStr = allStr;
            if minNum > allNum:
                minNum = allNum;
                minStr = allStr;

            dpMax[lower][higher] = maxNum;
            dpMin[lower][higher] = minNum;
            dpMaxStr[lower][higher] = maxStr;
            dpMinStr[lower][higher] = minStr;
            return maxStr;
        recur(0, len(nums))
        return dpMaxStr[0][len(nums)]

sol = Solution();
print(sol.optimalDivision([1000,100,10,2]))