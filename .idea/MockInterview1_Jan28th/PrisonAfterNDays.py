class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        mapping = {}
        if n == 0:
            return cells;
        def recur(cellStr: str, n: int):
            if n == 0:
                return cellStr;
            if cellStr in mapping:
                return mapping[cellStr]
            prevStr = recur(cellStr, n-1);
            lst = list(prevStr)
            lstCopy = lst.copy()
            lst[0] = '0';
            lst[len(lst)-1] = '0'
            for index in range(1, len(lstCopy)-1):
                if lstCopy[index-1] == lstCopy[index+1]:
                    lst[index] = '1';
                else:
                    lst[index] = '0';
            nextStr = ''.join(lst)
            mapping[prevStr] = nextStr
            return nextStr;

        lstStr = self.convertToStr(cells);
        finalStr = recur(lstStr, n)
        return self.convertToIntList(finalStr)

    def convertToStr(self, lst: list[int]):
        result = ""
        for num in lst:
            result += (str(num) + "");
        return result;

    def convertToIntList(self, string: str):
        lst = []
        for s in string:
            lst.append(int(s))
        return lst;

sol = Solution()
print(sol.prisonAfterNDays([1,0,0,1,0,0,1,0], 7))
