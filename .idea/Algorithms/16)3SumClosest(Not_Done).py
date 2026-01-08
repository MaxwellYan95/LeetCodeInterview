class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

    def recur(self, nums: list[int], target: int):
        if len(nums) == 3:
            return sum(nums)
        left = self.threeSumClosest(nums[1:])
        right = self.threeSumClosest(nums[:len(nums)-1])
        total1 = sum(nums[len(nums)-3: len(nums)])
        total2 = sum(nums[:len(nums)-3])
        total3 = sum(nums[len(nums)-2: len(nums)]) + nums[0]
        total4 = sum(nums[:2]) + nums[len(nums)-1];

