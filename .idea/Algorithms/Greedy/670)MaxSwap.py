class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = str(num)
        if len(numStr) == 1:
            return num
        for i in range(len(numStr)-1):
            n = int(numStr[i])
            digit, index = self.maxDigit(numStr[i+1:]);
            index += (i+1);
            if digit > n:
                return self.swap(numStr, i, index)
        return num

    # Returns digit and index
    def maxDigit(self, numStr: str):
        if len(numStr) == 0:
            return None;
        index = 0
        count = 0;
        digit = int(numStr[0])
        count += 1;
        for n in numStr[1:]:
            d = int(n)
            if d >= digit:
                digit = d
                index = count
            count += 1;
        return (digit, index)

    def swap(self, numStr: str, i1: int, i2: int):
        numList = list(numStr)
        temp = numList[i1]
        numList[i1] = numList[i2]
        numList[i2] = temp;
        return int(''.join(numList))


sol = Solution();
print(sol.maximumSwap(12))



