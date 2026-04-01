import bisect


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        costDict = {}
        keys = [1, 7, 30];
        for index in range(len(keys)):
            costDict[keys[index]] = costs[index];
        dp = [float('inf') for i in days];
        dp[0] = min(costs);
        for index in range(1, len(days)):
            dayCur = days[index]
            for dayNum, cost in costDict.items():
                prevDay = dayCur-dayNum
                if prevDay < days[0]:
                    dp[index] = min(dp[index], cost);
                else:
                    prevIndex = bisect.bisect_left(days, prevDay);
                    if prevDay not in days:
                        prevIndex -= 1;
                    dp[index] = min(dp[index], dp[prevIndex] + cost);
        return dp[len(dp)-1];

sol = Solution();
print(sol.mincostTickets([1,4,6,7,8,20], [2,7,15]))
