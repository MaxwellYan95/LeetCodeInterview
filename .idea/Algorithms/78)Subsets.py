class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = self.recur(nums);
        results.append([]);
        return results;

    def recur(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums];
        prev1 = self.recur(nums[:len(nums)-1]);
        prev2 = self.recur(nums[len(nums)-1:]);
        results = [];
        results.extend(prev1);
        results.extend(prev2);
        for lst in prev1:
            newLst = lst.copy();
            newLst.append(prev2[0][0]);
            results.append(newLst);
        return results;

sol = Solution();
print(sol.subsets([1,2,3]))