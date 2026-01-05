class Solution:
    # NOTE: Use Dynamic Programming
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1;
        result = 0;
        if dividend < 1:
            sign *= -1;
            dividend *= -1;
        if divisor < 1:
            sign *= -1;
            divisor *= -1;
        if divisor == dividend:
            return 0;
        if divisor == 1:
            return self.bounds(sign, dividend);
        while dividend >= divisor:
            result += 1;
            dividend -= divisor;
        return self.bounds(sign, result);

    def bounds(self, sign: int, quotient: int):
        minimum = -(2**31)
        maximum = 2**31 - 1
        if sign == -1:
            return max(minimum, sign * quotient)
        return min(maximum, sign * quotient)
