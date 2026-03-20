from collections import defaultdict

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervalSort = intervals.sort(key=lambda x: x[1]);
        startInd, endInd = intervals[0];
        result = 0;
        for start, end in intervals[1:]:
            if start >= endInd:
                endInd = end;
            else:
                result += 1;
        return result;

sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))



