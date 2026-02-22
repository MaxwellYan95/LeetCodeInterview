class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        map = {}
        map["D"] = "Dire"
        map["R"] = "Radiant"
        lst = list(senate);
        while len(lst) > 1:
            if "D" not in lst or "R" not in lst:
                return map[lst[0]]
            current = lst.pop(0);
            for i in range(len(lst)):
                if lst[i] != current:
                    lst.pop(i)
                    break;
            lst.append(current);
        return map[lst[0]]

sol = Solution()
print(sol.predictPartyVictory("DDR"))