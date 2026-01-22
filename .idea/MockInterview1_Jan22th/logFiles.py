class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letterLogs = [];
        digitLogs = [];
        for log in logs:
            identifier = log.split(" ")[0]
            str = log[len(identifier)+1:];
            if self.isDigitLog(str):
                digitLogs.append(identifier + " " + str);
            else:
                letterLogs.append([identifier, str]);
        letterLogs.sort(key = lambda x: x[0]);
        letterLogs.sort(key = lambda x: x[1]);
        notDigitLogs = [log[0] + " " + log[1] for log in letterLogs]
        return notDigitLogs + digitLogs


    def isDigitLog(self, log: str) -> bool:
        wholeStr = ""
        for char in log.split(" "):
            wholeStr += "" + char
        for char in list(wholeStr):
            if not self.isDigit(char):
                return False;
        return True;

    def isDigit(self, char: str) -> bool:
        cond = (char == '0') or (char == '1') or \
               (char == '2') or (char == '3') or \
               (char == '4') or (char == '5') or \
               (char == '6') or (char == '7') or \
               (char == '8') or (char == '9')
        return cond;
sol = Solution()
print(sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))