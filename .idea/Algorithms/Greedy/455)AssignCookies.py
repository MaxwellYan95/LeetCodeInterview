class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort();
        s.sort();
        count = 0;
        i = 0;
        j = 0;
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1;
                j += 1;
                count += 1;
            else:
                j += 1;
        return count;