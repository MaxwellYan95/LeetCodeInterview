class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        index = 0;
        n = len(temperatures)
        stack = [temperatures[0]]
        result = [0 for i in range(n)]
        while index < n:
            length = len(stack)-1;
            if stack[0]
        return result

sol = Solution()
print(sol.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
