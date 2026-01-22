class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Using two pass method
        # Forward iteration and THEN backward iteration
        res = -float('inf')
        maxMulti = 1;
        for n in nums[0:]:
            maxMulti *= n;
            res = max(res, maxMulti);
            if n == 0:
                maxMulti = 1;
        maxMulti = 1;
        for n in reversed(nums):
            maxMulti *= n;
            res = max(res, maxMulti);
            if n == 0:
                maxMulti = 1;
        return res;


sol = Solution();
print(sol.maxProduct([3, -1, 4]))