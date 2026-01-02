class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matrix = [[False for inner in range(len(p)+1)] for out in range(len(s)+1)];

        # Initializes matrix[0][0]
        if p[0] == '*' or p[0] == '.' or p[0] == s[0]:
            matrix[0][0] = True;
        else:
            matrix[0][0] = False;

        # Initializes matrix[0][s]
        for x in range(1, len(s)+1):
            if p[0] == '*':
                matrix[x][0] = True;
            else:
                matrix[x][0] = False;
        for x in range(len(s)):
            for y in range(1, len(p)+1):
                if y == 0 and x == 0:
                    continue;
                elif p[y] == '.':
                    if x-1 < 0:
                        matrix[x][y] = False;
                    else:
                        matrix[x][y] = matrix[x-1][y-1];
                elif p[y] == '*':
                    if p[y-1] == '.':
                        matrix[x][y] = True;
                    else:
                        matrix[x][y] = s[x] == p[y-1];
                elif p[y] == s[x]:
                    matrix[x][y] = matrix[x][y-1];
                else:
                    matrix[x][y] = False;
        return matrix[len(s)-1][len(p)-1]


sol = Solution();
print(sol.isMatch("aab", "c*a*b"))
