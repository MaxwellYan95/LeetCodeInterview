class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # what if the final maximum is negative
        maximum = -float('inf')
        # consider that -1*-1 = 1
        result = 1;
        for n in nums:
            result *= n
            maximum = max(result, maximum);
            if n == 0:
                result = 1;
        result = 1;
        for n in reversed(nums):
            result *= n
            maximum = max(result, maximum);
            if n == 0:
                result = 1;
        return maximum



sol = Solution();
print(sol.maxProduct([2,3,-2,4]))