class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        maxLen = 0;
        for n in nums:
            maxLen = max(len(str(n)), maxLen)
        nums.sort(key = lambda x: str(x) * maxLen, reverse=True)
        result = ""
        for n in nums:
            result += str(n);
        if result[0] == '0':
            return str(0);
        return result

sol = Solution()
print(sol.largestNumber([3,30,34,5,9]))

