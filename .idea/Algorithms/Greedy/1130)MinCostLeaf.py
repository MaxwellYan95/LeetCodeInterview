import heapq


class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        # I FORGOT to add float('inf')
        stack = [float('inf')];
        total = 0;
        # I FORGOT that each leaf in an in-order traversal
        for num in arr:
            # Finding a local maxima/minima
            while stack[-1] < num:
                middle = stack.pop();
                # num is the right adj node of middle
                # REMEMBER: stack[-1] is different because stack.pop() was called
                # That means stack[-1] is the left adj node of middle
                total += middle * min(num, stack[-1]);
            stack.append(num)
        # Has to be > and not >=
        # Explanation: What if there is a root node?
        while len(stack) > 2:
            total += stack.pop() * stack[-1]
        return total


sol = Solution();
print(sol.mctFromLeafValues([7, 12, 8, 10]))


