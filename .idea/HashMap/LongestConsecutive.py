class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sortNums = sorted(set(nums));
        result = 1;
        curResult = 1;
        inSeq = False;
        for index in range(len(sortNums)-1):
            first = sortNums[index];
            second = sortNums[index+1];
            if (second-first == 1):
                curResult += 1;
            else:
                result = max(result, curResult);
                curResult = 1;
        result = max(result, curResult);
        return result;

sol = Solution();
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]));
