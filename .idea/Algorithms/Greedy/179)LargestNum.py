class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        maxLen = 0;
        for n in nums:
            maxLen = max(len(str(n)), maxLen)
        nums.sort(lambda x: str(x) * maxLen)
        result = ""
        for n in nums:
            result += str(n);
        return result

sol = Solution()
print(sol.largestNumber([3,30,34,5,9]))

