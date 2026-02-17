class Solution:
    def reverseWords(self, s: str) -> str:
        sLst = s.split(" ")
        result = ""
        for word in sLst[::-1]:
            if len(word) > 0:
                result += word + ' '
        return result[:len(result)-1]

sol = Solution()
print(sol.reverseWords("   sdfsdf    dsgasg   "))