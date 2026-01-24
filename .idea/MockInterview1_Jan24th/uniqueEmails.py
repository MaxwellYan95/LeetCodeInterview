class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        allEmails = [];
        for e in emails:
            format = e.split("@")
            name = self.localName(format[0]);
            if (name, format[1]) not in allEmails:
                allEmails.append((name, format[1]))
        return len(allEmails);


    def localName(self, name: str):
        result = "";
        for char in name:
            if char == '+':
                break;
            if char != '.':
                result += char
        return result
sol = Solution()
print(sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))