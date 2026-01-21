class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccur = {};
        stack = []; # stack is FIFO (First-In, First-Out)
        visited = set();
        for i in range(len(s)):
            lastOccur[s[i]] = i;
        for index in range(len(s)):
            char = s[index]
            if char not in visited:
                # stack[-1] is the last element of the stack
                while stack and stack[-1] > char and index < lastOccur[stack[-1]]:
                    prev = stack.pop();
                    visited.remove(prev);
                stack.append(char);
                visited.add(char);
        return ''.join(stack)


sol = Solution()
print(sol.removeDuplicateLetters("acdbc"))