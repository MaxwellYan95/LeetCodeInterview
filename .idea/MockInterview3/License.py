class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        noDash = ""
        for subS in s.split("-"):
            noDash += subS.upper();
        remainInt = len(noDash) % k;
        result = ""
        beg = 0;
        end = k;
        if remainInt != 0:
            result += (noDash[:remainInt] + "-");
            beg = remainInt;
            end = remainInt+k;
        while end <= len(noDash):
            result += (noDash[beg:end] + "-")
            beg += k;
            end += k;
        return result[:len(result)-1]

sol = Solution()
print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))