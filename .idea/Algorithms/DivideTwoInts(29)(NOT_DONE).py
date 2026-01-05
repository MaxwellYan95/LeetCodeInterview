class Solution:
    # NOTE: Use Dynamic Programming
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1;
        quotient = 0;

        if dividend < 1:
            sign *= -1;
            dividend *= -1;
        if divisor < 1:
            sign *= -1;
            divisor *= -1;

        # dividend to quotient
        map = dict();
        maxDiv = divisor;
        map[divisor] = 1;

        if divisor == dividend:
            return sign*1;
        if divisor == 1:
            return self.bounds(sign, dividend);
        number = divisor;
        while dividend >= maxDiv:
            dividend -= maxDiv;
            quotient += map[maxDiv]
            map[maxDiv+maxDiv] = map[maxDiv] + map[maxDiv]
            maxDiv = maxDiv+maxDiv;
        while dividend >= divisor:
            if dividend in map:
                quotient += map[dividend];
                return self.bounds(sign, quotient);
            quotient += 1;
            dividend -= divisor;
        return self.bounds(sign, quotient);

    def bounds(self, sign: int, quotient: int):
        minimum = -(2**31)
        maximum = 2**31 - 1
        quotient *= sign
        if quotient > maximum:
            return maximum
        if quotient < minimum:
            return minimum
        return quotient;

sol = Solution();
print(sol.divide(-2147483648, 2));