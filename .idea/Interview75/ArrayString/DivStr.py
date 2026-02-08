class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0] != str2[0]:
            return ""
        divisor = self.gcd(len(str1), len(str2))
        commonStr = str1[:divisor]
        for index in range(0, len(str1), divisor):
            subStr1 = str1[index: index+divisor]
            if subStr1 != commonStr:
                return ""
        for index in range(0, len(str2), divisor):
            subStr2 = str2[index: index+divisor]
            if subStr2 != commonStr:
                return ""
        return commonStr

    def gcd(self, n1: int, n2: int):
        minimum = min(n1, n2)
        result = 1;
        for n in range(1, minimum+1):
            if n1 % n == 0 and n2 % n == 0:
                result = max(result, n)
        return result

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))