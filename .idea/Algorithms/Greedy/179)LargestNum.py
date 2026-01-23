class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        numStr = [str(n) for n in nums];
        maxLen = 1;
        numStr.sort(key=lambda x: x[len(x)-1])
        numStr.sort(key=lambda x: x[0]);
        numStr = reversed(numStr)
        result = ""
        for s in numStr:
            result += "" + s;
        return result;

sol = Solution()
print('x' > '9')
print(sol.largestNumber([3,30,34,5,9]))

