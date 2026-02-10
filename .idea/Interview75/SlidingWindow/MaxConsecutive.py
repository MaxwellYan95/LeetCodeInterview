class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        low = 0;
        high = 1;
        result = 0;
        kCount = 0;
        if nums[0] == 1:
            result = 1;
        else:
            kCount += 1;
        high += 1;
        while high <= len(nums):
            if nums[high-1] == 0:
                kCount += 1;
            while kCount > k:
                if nums[low] == 0:
                    kCount -= 1;
                low += 1;
            result = max(result, high-low);
            high += 1
        if kCount <= k:
            result = max(result, high-low-1);
        return result

sol = Solution()
print(sol.longestOnes([0,0,0,1], 4))