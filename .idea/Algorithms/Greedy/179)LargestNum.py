class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # You want to compare the first digit.
        # If the first digit is the same, compare the second digit.
        # If the second digit is the same, compare the third digit.
        # Vice versa

        # 30 has lower priority than 3.
        # 34 has higher priority than 3,
        # This is because the greater digit should always come first.
        numStr = [str(n) for n in nums];

        # REMEMBER: 0 <= nums[i] <= 10^9
        # That's why you are using "lambda x: x*10"
        numStr.sort(key=lambda x: x*10, reverse=True);
        result = ""
        if numStr[0] == "0":
            return "0";
        for s in numStr:
            result += "" + s;
        return result;

sol = Solution()
print('x' > '9')
print(sol.largestNumber([3,30,34,5,9]))

