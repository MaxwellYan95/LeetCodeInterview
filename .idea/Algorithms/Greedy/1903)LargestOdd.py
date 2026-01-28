class Solution:
    def largestOddNumber(self, num: str) -> str:
        high = -1;
        for index in range(len(num)-1, -1, -1):
            digit = int(num[index])
            if digit % 2 != 0:
                high = index+1;
                break;
        if high == -1:
            return ""
        return num[:high];
sol = Solution()
print(sol.largestOddNumber("52"))