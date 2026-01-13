from collections import defaultdict

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        equation = self.equation(expression);
        dp = defaultdict(list);
        for i in range(0, len(equation), 2):
            dp[(i, i+1)].append(int(equation[i]))

        def recur(lower: int, higher: int) -> list[int]:
            results = [];
            if (lower, higher) in dp:
                return dp[(lower, higher)];
            for i in range(lower+2, higher, 2):
                oper = equation[i-1];
                left = recur(lower, i-1);
                right = recur(i, higher)
                for l in left:
                    for r in right:
                        if oper == '+':
                            results.append(l + r);
                        elif oper == '-':
                            results.append(l - r);
                        else:
                            results.append(l * r);
            dp[(lower, higher)] = results;
            return results;
        return recur(0, len(equation))

    def equation(self, expression: str) -> list[str]:
        beg = 0;
        equa = [];
        for index in range(len(expression)):
            isOper = expression[index] == '+' \
                     or expression[index] == '-' \
                     or expression[index] == '*'
            if isOper:
                equa.append(expression[beg: index]);
                beg = index+1;
                equa.append(expression[index]);
        equa.append(expression[beg:]);
        return equa;
sol = Solution();
print(sol.diffWaysToCompute("2*3-4*5"))