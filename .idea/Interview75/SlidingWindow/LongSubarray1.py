class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if 0 not in nums:
            return len(nums)-1;
        while len(nums) > 0 and nums[0] == 0:
            nums.pop(0);
        if len(nums) == 0:
            return 0;
        prevOnes = 0;
        ones = 0;
        results = 0;
        index = 0;
        while index < len(nums):
            if nums[index] == 0:
                results = max(results, prevOnes+ones)
                prevOnes=ones;
                ones=0;
                index+=1;
                while index < len(nums) and nums[index] == 0:
                    prevOnes=0;
                    index+=1;
            else:
                index+=1;
                ones+=1;
        if ones != 0:
            results = max(results, prevOnes+ones);
        return results;

sol = Solution()
print(sol.longestSubarray([1,1,0,0,1,1,1,0,1]))
