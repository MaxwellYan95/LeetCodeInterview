class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        def recur(costs: list[list[int]], isA: bool):
            i2 = 1;
            if isA:
                i2 = 0
            if len(costs) == 1:
                return costs[0][i2]
            minIndex = 0;
            minVal = costs[0][i2]
            secVal = costs[0][(i2+1) % 2]
            for i1 in range(1, len(costs)):
                c = costs[i1]
                if minVal > c[i2]:
                    minVal = c[i2];
                    minIndex = i1;
                    secVal = c[(i2+1) % 2]
                if minVal == c[i2] and secVal > c[(i2+1) % 2]:
                    minVal = c[i2];
                    minIndex = i1;
                    secVal = c[(i2+1) % 2]
            subCost = costs[:minIndex] + costs[minIndex+1:];
            return minVal + recur(subCost, not isA)
        startA = recur(costs, True);
        startB = recur(costs, False);
        return min(startA, startB)


sol = Solution()
print(sol.twoCitySchedCost([[70,311],[74,927],[732,711],[126,583],[857,118],[97,928],[975,843],[175,221],[284,929],[816,602],[689,863],[721,888]]))