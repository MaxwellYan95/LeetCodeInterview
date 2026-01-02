class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        if (k == 1):
            return [[num] for num in range(1, n+1)]
        lst = self.combine(n, k-1)
        newLst = []
        for innerLst in lst:
            for num in range(innerLst[len(innerLst)-1]+1, n+1):
                addLst = innerLst.copy()
                addLst.append(num)
                newLst.append(addLst)
        return newLst

sol = Solution()
print(sol.combine(4, 2))