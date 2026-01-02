class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = float('-inf');
        total = 0;
        for n in nums:
            total += n;
            maximum = max(total, maximum);
            if total < 0:
                total = 0;
        return maximum;


sol = Solution();
print(sol.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]));
