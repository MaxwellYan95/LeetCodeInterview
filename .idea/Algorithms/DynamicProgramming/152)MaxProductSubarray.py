class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxMulti = nums[0];
        multi = 1;
        for n in nums:
            multi *= n;
            maxMulti = max(multi, maxMulti);
            if n == 0:
                multi = 1;
        multi = 1;
        for n in nums[::-1]:
            multi *= n;
            maxMulti = max(multi, maxMulti);
            if n == 0:
                multi = 1;
        return maxMulti;

sol = Solution();
print(sol.maxProduct([2,3,-2,4]))