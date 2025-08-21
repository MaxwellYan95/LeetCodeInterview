class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return "";
        if s == t:
            return s;
        sub, window = {}, {}
        for c in t:
            sub[c] = sub.get(c, 0) + 1;
        have = 0;
        need = len(sub);
        left = 0;
        res = [-1, -1];
        subLen = float("infinity");
        for right in range(len(s)):
            c = s[right];
            window[c] = window.get(c, 0) + 1;
            if c in sub and window[c] == sub[c]:
                have += 1;
            while need == have:
                if (right - left + 1) < subLen:
                    res = [left, right];
                    subLen = right - left + 1;
                window[s[left]] -= 1;
                if s[left] in sub and window[s[left]] < sub[s[left]]:
                    have -= 1;
                left += 1;
        if subLen == float("infinity"):
            return "";
        left, right = res;
        return s[left: right+1];

sol = Solution();
print(sol.minWindow("ADOBECODEBANC", "ABC"))