class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort();
        count = 1;
        prev = nums[0];
        for n in nums[1:]:
            if prev != n:
                count = 1;
                prev = n;
            else:
                count += 1;
                if count > len(nums) // 2:
                    return n;
        return -1;

sol = Solution();
print(sol.majorityElement([3,2,3]))