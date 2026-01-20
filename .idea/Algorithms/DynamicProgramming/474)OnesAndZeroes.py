class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = {(0,0): 0}
        for s in strs:
            one = s.count("1");
            zero = s.count("0")
            newDp = {};
            for (dpOne, dpZero), val in dp.items():
                newOne = dpOne+one;
                newZero = dpZero+zero;
                if newOne <= n and newZero <= m:
                    if (dpOne+one, dpZero+zero) not in dp:
                        newDp[(dpOne+one, dpZero+zero)] = val+1;
                    elif dp[(dpOne+one, dpZero+zero)] < val+1:
                        newDp[(dpOne+one, dpZero+zero)] = val+1;
            dp.update(newDp)
        return max(dp.values())




sol = Solution()
res = sol.findMaxForm(["10","0001","111001","1","0"], 5, 3)
print()

