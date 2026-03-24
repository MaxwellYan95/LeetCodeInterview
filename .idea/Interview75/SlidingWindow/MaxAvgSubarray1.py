class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = 0;
        for n in nums[:k]:
            total += n;
        maxAvg = total / k;
        begin = 0;
        end = k;
        for i in range(k, len(nums)):
            total -= nums[i - k];
            total += nums[i];
            maxAvg = max(maxAvg, total / k)
        return maxAvg