import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        stack = nums.copy()
        heapq.heapify(stack);
        count = 0
        while count != k:
            n = heapq.heappop(stack);
            heapq.heappush(stack, -1*n)
            count += 1;
        return sum(stack)

sol = Solution()
print(sol.largestSumAfterKNegations([2,-3,-1,5,-4], 2))
