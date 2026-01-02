class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ind = self.findIndex(nums);
        if (nums[0] <= target and nums[ind] >= target):
            return self.traverse(nums[:ind+1], target);
        right = self.traverse(nums[ind+1:], target);
        if right == -1:
            return -1;
        return ind+1 + self.traverse(nums[ind+1:], target);

    def findIndex(self, nums: list[int]):
        if len(nums) == 1:
            return 0;
        elif len(nums) == 2:
            if nums[0] < nums[1]:
                return 1;
            else:
                return 0;
        if nums[0] < nums[len(nums)-1]:
            return len(nums)-1;
        middleIndex = int(len(nums)/2);
        if (nums[0] < nums[middleIndex]):
            return middleIndex + self.findIndex(nums[middleIndex:]);
        else:
            return self.findIndex(nums[:middleIndex+1]);

    def traverse(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1;
        elif len(nums) == 1:
            if nums[0] == target:
                return 0;
            return -1;
        elif len(nums) == 2:
            if target == nums[1]:
                return 1;
            elif target == nums[0]:
                return 0;
            return -1;
        middleInd = int(len(nums)/2);
        middleElem = nums[middleInd];
        if nums[0] <= target and middleElem >= target:
            return self.traverse(nums[:middleInd+1], target);
        right = self.traverse(nums[middleInd:], target);
        if (right == -1):
            return -1;
        return middleInd + self.traverse(nums[middleInd:], target);

sol = Solution();
print(sol.search([4,5,6,7,0,1,2], 3));
print(sol.search([4,5,6,7,0,1,2], 0));
print(sol.search([6,7,1,2,3,4,5], 6));
print(sol.search([1], 0));
print(sol.search([1, 3], 0));
print();