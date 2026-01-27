class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        starts = 0;
        ends = 0;
        for p in s:
            if p == ')':
                if starts == 0:
                    ends += 1;
                else:
                    starts -= 1;
            elif p == '(':
                starts += 1;
        return starts + ends;