class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        beg = 0;
        end = min(len(s), k);
        result = "";
        rev = True;
        while end < len(s):
            if rev:
                result += self.reverse(s[beg:end]) + "";
                rev = False;
            else:
                result += s[beg:end] + "";
                rev = True;
            beg += k;
            end = min(len(s), end+k);
        if rev:
            result += self.reverse(s[beg:end]) + "";
        else:
            result += s[beg:end] + "";
        return result;

    def reverse(self, s: str):
        result = ""
        for index in range(len(s)-1, -1, -1):
            result += s[index] + "";
        return result;

sol = Solution();
print(sol.reverseStr("abcdefg", 2));