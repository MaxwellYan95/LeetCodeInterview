class Solution:
    def lengthLongestPath(self, input: str) -> int:
        order = 0;
        lineLst = input.split("\n")
        curDir = []
        longestPath = 0;
        for line in lineLst:
            order = 0
            beg = 0;
            end = 1;
            while line[beg:end] == "\t":
                order += 1;
                beg += 1;
                end += 1;
            curLoc = line[beg:]
            if len(curDir) < order+1:
                curDir.append(curLoc)
            else:
                curDir[order] = curLoc
            if '.' in curLoc:
                curLen = self.getPath(curDir[:order+1]);
                longestPath = max(longestPath, curLen)
        return longestPath;


    def getPath(self, curDir: list):
        length = 0;
        length += len(curDir[0]);
        for dir in curDir[1:]:
            length += (len(dir) + 1)
        return length

sol = Solution()
print(sol.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))