class Solution:



    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = [];
        if (target < min(candidates)):
            return [];
        for index in range(len(candidates)):
            num = candidates[index];
            if target == num:
                result.append([num]);
            lst = self.combinationSum(candidates[index:], target-num)
            for innerLst in lst:
                if len(innerLst) > 0:
                    innerLstCopy = innerLst.copy();
                    innerLstCopy.insert(0, num);
                    result.append(innerLstCopy);
        return result;

sol = Solution();
lst = sol.combinationSum([2,3,6,7], 7);
print(lst);