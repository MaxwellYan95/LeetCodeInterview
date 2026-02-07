class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vIndex = 0;
        stack = []
        curVowels = [];
        for char in s:
            stack.append(char)
            if char in vowels:
                curVowels.append(char);

        for index in range(len(stack)):
            char = stack[index]
            if char in vowels:
                stack[index] = curVowels[len(curVowels)-1]
                curVowels = curVowels[:len(curVowels)-1]
        return ''.join(stack)

sol = Solution()
print(sol.reverseVowels("IceCreAm"))