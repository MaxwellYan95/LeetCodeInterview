class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums);
        move = [0] * n;
        if len(nums) == 0:
            return 0;
        if len(nums) == 1:
            return nums[0];
        move[0] = nums[0];
        move[1] = max(nums[1], nums[0]);
        for i in range(2, n):
            move[i] = max(move[i-1], nums[i] + move[i-2]);
        return move[len(move)-1];

sol = Solution();
sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]);