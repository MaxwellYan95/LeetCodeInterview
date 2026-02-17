class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        if len(bits) == 1:
            return True;
        if len(bits) == 2:
            return bits[0] == 1;
        return self.isOneBitCharacter(bits[1:]) or self.isOneBitCharacter(bits[2:])

sol = Solution()
print(sol.isOneBitCharacter([1,0,0]))