class Solution:

    # PAY ATTENTION to last bit. It's a 0
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        return self.secondLastIsOne(bits) and self.secondLastIsOne(bits[1:])

    def secondLastIsOne(self, bits: list[int]):
        if len(bits) == 0:
            return True;
        index = 0;
        for i in range(0, len(bits), 2):
            index = i;
        return bits[index] != 1;

sol = Solution()
print(sol.isOneBitCharacter([0]))