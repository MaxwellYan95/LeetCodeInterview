class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index = 0;
        sList = list(s);
        if (len(s) == k):
            return reversed(s);
        while True:
            if index+k <= len(s):
                reverse = index+k-1;
                for i in range(index, index+k):
                    sList[i] = s[reverse];
                    reverse -= 1;
                index += (2*k);
            else:
                break;
        return "".join(sList);

sol = Solution();
print(sol.reverseStr("abcdefg", 8));