from collections import defaultdict

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        results = [];
        zeros = 0;
        twos = 0;
        mapping = defaultdict(int)
        for n in nums:
            mapping[n] += 1;
        index = 0;
        keyLst = [0, 1, 2]
        for key in keyLst:
            for count in range(mapping[key]):
                nums[index] = key;
                index += 1;

sol = Solution()
num1 = [2,0,2,1,1,0]
sol.sortColors(num1)
print(num1)