class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        results = [1 for n in nums];
        for index in range(len(nums)-2, -1, -1):
            for inner in range(index+1, len(nums)):
                if nums[index] < nums[inner]:
                    results[index] = max(1+results[inner], results[index]);
        return max(results);

sol = Solution();
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]));