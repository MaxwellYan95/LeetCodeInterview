class Solution:
    mapping = {};

    def partition(self, s: str) -> list[list[str]]:
        if len(s) == 1:
            self.mapping[s] = [[s]]
            return self.mapping[s]
        results = [];
        for index in range(1,len(s)+1):
            if s[index-1] not in self.mapping:
                self.mapping[s[index-1]] = [[s[index-1]]]
            elif s[:index] in self.mapping:
                results.extend(self.mapping[s[:index]])
            else:
                if self.isPartition(s[:index]):
                    results.append([s[:index]])
                    results.extend(self.partition(s[:index]))
        self.mapping[s] = results;
        return results


    def isPartition(self, s: str):
        beg = 0;
        end = len(s)-1;
        while beg < end:
            if s[beg] != s[end]:
                return False
            beg += 1;
            end -= 1;
        return True;

sol = Solution()
print(sol.partition("aab"))