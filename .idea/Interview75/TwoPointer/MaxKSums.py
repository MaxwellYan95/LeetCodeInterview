class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        index = 0;
        count = 0;
        while len(nums) > 1 and index < len(nums):
            n1 = nums[index];
            n2 = k-nums[index]
            if n2 in nums[index+1:]:
                nums.remove(n1);
                nums.remove(n2);
                count += 1;
            else:
                index += 1;
        return count
sol = Solution()
print(sol.maxOperations([3,1,5,1,1,1,1,1,2,2,3,2,2]
                        , 1))

