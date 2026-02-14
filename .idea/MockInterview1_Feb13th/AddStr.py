class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        excess = max(len(num1), len(num2)) - min(len(num1), len(num2));
        if len(num1) < len(num2):
            num1 = ''.join(["0" for i in range(excess)]) + num1;
        else:
            num2 = ''.join(["0" for i in range(excess)]) + num2;
        index = len(num2) - 1;
        carry = 0;
        result = ""
        while index >= 0:
            d1 = int(num1[index])
            d2 = int(num2[index])
            added = d1 + d2 + carry
            if added >= 10:
                added = added % 10;
                carry = 1;
            else:
                carry = 0;
            result = str(added) + result;
            index -= 1;
        if carry == 1:
            result = str(carry) + result;
        return result;
sol = Solution()
print(sol.addStrings("1", "9"))

