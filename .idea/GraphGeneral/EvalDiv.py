class charAndNumber:
    def __init__(self, letter: str, number: float):
        self.letter = letter;
        self.number = number;
    def getLetter(self):
        return self.letter;
    def getNumber(self):
        return self.number;

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        def variables(equations: list[list[str]], values: list[float]):
            var = {};
            for index in range(len(equations)):
                equa = equations[index]
                firstC = equa[0];
                secondC = equa[1];
                if firstC in var:
                    var[firstC].append(charAndNumber(secondC, values[index]));
                else:
                    var[firstC] = [charAndNumber(secondC, values[index])];
                if secondC in var:
                    var[secondC].append(charAndNumber(1/float(values[index]), firstC));
                else:
                    var[secondC] = [charAndNumber(1/float(values[index]), firstC)];
            return var;
        substitute = variables(equations, values);
        nums = [];
        for q in queries:
            found = False;
            q1 = q[0];
            q2 = q[1];
            if q1 in substitute:
                for sub in substitute[q1]:
                    if q2 == sub.letter:
                        nums.append(1/sub.number);
                        found = True;
                        break;
            if (found == True):
                continue;
            if q2 in substitute:
                for sub in substitute[q2]:
                    if q1 == sub.letter:
                        nums.append(sub.number);
                        found = True;
                        break;
            if (found == True):
                continue;
            else:
                nums.append(-1);
        return nums;

sol = Solution();
print(sol.calcEquation([["a","b"],["b","c"]], [2, 3], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))