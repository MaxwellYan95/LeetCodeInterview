class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [temperatures[0]];
        i1 = 0;
        i2 = 1;
        results = [];
        while len(stack) < len(temperatures):
            stack.append(temperatures[i2]);
            if stack[i1] < stack[i2]:
                minIndex = i2-i1
                while i2-i1 >= 1:
                    if stack[i1] < stack[i2]:
                        minIndex = i2-i1
                    stack.pop(len(stack)-1)
                    i2 -= 1;
                results.append(minIndex);
                i1 += 1;
            i2 += 1;
        i2 -= 1
        while len(results) < len(temperatures):
            minIndex = 0
            while i2-i1 >= 1:
                if stack[i1] < stack[i2]:
                    minIndex = i2-i1
                i2 -= 1;
            results.append(minIndex);
            i1 += 1;
            i2 = len(stack)-1;
        return results



sol = Solution()
print(sol.dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))
