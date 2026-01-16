from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = defaultdict(int)
        dp[(1, nums[0])] = 1;
        dp[(1, -nums[0])] = 1;
        def recur(upBound: int, subTarget):
            if upBound == 1:
                if subTarget == 0:
                    return dp[(upBound, subTarget)] + dp[(upBound, subTarget)];
                return dp[(upBound, subTarget)];
            elif dp[(upBound, subTarget)] != 0:
                return dp[(upBound, subTarget)]
            else:
                result = recur(upBound - 1, subTarget - nums[upBound - 1]) + recur(upBound - 1, subTarget + nums[upBound - 1]);
                dp[(upBound, subTarget)] = result;
                return result;
        return recur(len(nums), target);
