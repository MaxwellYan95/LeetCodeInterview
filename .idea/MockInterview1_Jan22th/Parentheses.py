class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ["()"]
        prevRes = self.generateParenthesis(n-1);
        result = set();
        for str in prevRes:
            for index in range(len(str)):
                result.add(str[:index] + "()" + str[index:]);
        return list(result)
