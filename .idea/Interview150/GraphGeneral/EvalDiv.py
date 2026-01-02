class Solution:

    def makeDict(self, equations: list[list[str]], values: list[float]):
        eq_dict = dict();
        for index in range(len(values)):
            n1, n2 = equations[index];
            val = values[index];
            if n1 not in eq_dict.keys():
                eq_dict[n1] = [[n2, val]];
            else:
                eq_dict[n1].append([n2, val])
            if n2 not in eq_dict.keys():
                eq_dict[n2] = [[n1, 1/val]];
            else:
                eq_dict[n2].append([n1, 1/val]);
        return eq_dict;
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        eq_dict = self.makeDict(equations, values);
        def dfs(temp_dict: dict, query: list[str]):
            if query[0] not in temp_dict:
                return -1;
            eq_values = temp_dict[query[0]];
            for num, val in eq_values:
                if (num == query[1]):
                    return val;
                temp_dict[query[0]] = temp_dict[query[0]][1:];
                recur = dfs(temp_dict, [num, query[1]]);
                if recur != -1:
                    return val*recur;
            return -1;

        results = [];
        for query in queries:
            val = dfs(eq_dict.copy(), query);
            results.append(val);
        return results;



sol = Solution();
print(sol.calcEquation([["a","b"],["b","c"]], [2, 3], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))