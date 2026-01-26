from collections import defaultdict

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        count = 0;
        finalLen = len(num) - k;
        for digit in num:
            while len(stack) > 0 and count < k and int(stack[len(stack)-1]) > int(digit):
                stack.pop();
                count += 1;
            stack.append(digit);
        if len(stack) > finalLen:
            stack = stack[:finalLen]

        # lstrip() removes characters from the left of the string
        result = ''.join(stack).lstrip('0');
        if result == '':
            return '0'
        return result;
sol = Solution()
print(sol.removeKdigits("1432219", 3))