class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if int(num1) < int(num2):
            temp = num2;
            num2 = num1;
            num1 = temp;
        lst = [];
        place = 1;
        for n2 in reversed(num2):
            lst.append(self.multiplyOne(int(num1), int(n2))*place);
            place *= 10;
        total = 0;
        for num in lst:
            total += num;
        return str(total)

    def multiplyOne(self, num1: int, num2: int):
        return num1*num2;

sol = Solution()
print(sol.multiply("123", "456"))