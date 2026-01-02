class Solution:

    map = dict()
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = [];
        if target < min(candidates):
            return results;
        for index in range(len(candidates)):
            num = candidates[index];
            if num == target:
                results.append([target]);
            innerRes = self.combinationSum(candidates[index:], target-num);
            for lst in innerRes:
                lstCopy = lst.copy()
                lstCopy.append(num)
                results.append(lstCopy)
        return results;


sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))