class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return [];
        elif n == 1:
            return ["()"];
        else:
            result = [];
            lst = self.generateParenthesis(n-1);
            for string in lst:
                for index in range(len(string)+1):
                    leftStr = string[0:index];
                    rightStr = string[index:];
                    newStr = str(leftStr) + "()" + str(rightStr);
                    if newStr not in result:
                        result.append(newStr);
            return result;

sol = Solution();
print(sol.generateParenthesis(3));