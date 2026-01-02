class Solution:
    def reverse(self, x: int) -> int:
        allDigits = self.digits(x);
        place = 1;
        for i in range(len(allDigits)-1):
            place *= 10;
        result = 0;
        for d in allDigits:
            result += (d*place);
            place = place / 10;
        result = int(result);
        if x < 0:
            result = -1 * result;
        if result < -(2 ** 31) or result > (2**31 - 1):
            return 0;
        return result;

    def digits(self, x: int) -> list[int]:
        copyX = x;
        if x < 0:
            copyX = -x;
        allDigits = [];
        while copyX != 0:
            allDigits.append(copyX%10);
            copyX = copyX//10;
        return allDigits;

sol = Solution();
sol.reverse(-123);