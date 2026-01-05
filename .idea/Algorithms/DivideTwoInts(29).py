class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        minimum = -2**31
        maximum = 2**31 - 1
        sign = 1;
        result = 0;
        if dividend < 1:
            sign *= -1;
            dividend *= -1;
        if divisor < 1:
            sign *= -1;
            divisor *= -1;
        while dividend >= divisor:
            result += 1;
            dividend -= divisor;
            inRange = (sign == -1 and -result > minimum) or (sign == 1 and result < maximum):
            if not inRange:
                break;
        return sign * result;
