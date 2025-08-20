class Solution:
    def calculate(self, s: str) -> int:
        sList = list(s)
        index = 0
        startIndex = 0
        endIndex = 0
        while "(" in sList or ")" in sList:
            endIndex = s.index(")")
            startIndex = s[0:endIndex].index("(")
            sub = sList[startIndex+1: endIndex]
            num = self.compute(list(sub))
            s = s[0:startIndex] + str(num) + s[endIndex+1: len(s)]
            sList = list(s)

        return self.compute(sList)

    def compute(self, s: list[str]) -> int:
        result = 0
        index = 0
        positive = True
        while True:
            if (index == len(s)):
                break
            elif s[index] == "+":
                positive = positive
                index += 1
            elif s[index] == "-":
                positive = not positive
                index += 1
            elif s[index].isnumeric():
                digits = []
                while s[index].isnumeric():
                    digits.append(s[index])
                    index = index + 1
                    if (index == len(s)):
                        break
                number = 0
                place = 0
                for d in reversed(digits):
                    number = number + (int(d)*(10**place))
                    place += 1
                if positive == True:
                    result += number
                else:
                    result -= number
                positive = True
            else:
                index += 1
        return result



sol = Solution()
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
print(sol.calculate("1-(    -2)"))
print(sol.calculate(" 2-1 + 2 "))

