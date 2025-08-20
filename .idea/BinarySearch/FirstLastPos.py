class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1];
        ind = self.firstInd(nums, target);
        if ind == -1:
            return [-1, -1];
        else:
            begInd = ind;
            endInd = ind;
            while nums[begInd] == target:
                begInd = begInd - 1;
                if begInd == -1:
                    break;
            begInd = begInd + 1;
            while nums[endInd] == target:
                endInd = endInd + 1;
                if endInd == len(nums):
                    break;
            endInd = endInd - 1;
            return [begInd, endInd];

    def firstInd(self, nums: List[int], target: int) -> int:
        middleInd = int(len(nums)/2);
        middleElem = nums[middleInd];
        if len(nums) == 1:
            if nums[0] == target:
                return 0;
            return -1;
        if nums[0] == target:
            return 0;
        elif nums[len(nums)-1] == target:
            return len(nums)-1;
        elif middleElem == target:
            return middleInd;
        if nums[0] < target and target < middleElem:
            return self.firstInd(nums[:middleInd], target);
        else:
            right = self.firstInd(nums[middleInd:], target);
            if right == -1:
                return -1;
            return middleInd + self.firstInd(nums[middleInd:], target);