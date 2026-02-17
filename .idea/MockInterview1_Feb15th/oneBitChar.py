class Solution:

    # PAY ATTENTION to last bit. It's a 0
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        index = 0;
        result = False;
        while index < len(bits):
            if bits[index] == 1:
                index += 2;
                result = False;
            else:
                index += 1;
                result = True;
        return result

sol = Solution()
print(sol.isOneBitCharacter([0]))