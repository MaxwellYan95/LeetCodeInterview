class Solution:
    # use sliding window
    def decodeString(self, s: str) -> str:
        stack = []
        index = 0;
        while index < len(s):
            char = s[index]
            stack.append(char);
            if char == ']':
                stack.pop()
                letter = ""
                num = ""
                while stack and stack[len(stack)-1].isalpha():
                    letter = str(stack.pop()) + letter
                stack.pop()
                while stack and stack[len(stack)-1].isnumeric():
                    num += str(stack.pop())
                num = num[::-1]
                num = int(num)
                stack.append(num * letter)
            index += 1;
        return ''.join(stack)


sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
