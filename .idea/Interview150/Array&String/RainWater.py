class Solution:
    def trap(self, height: list[int]) -> int:
        maxLeft = [0] * len(height);
        maxRight = [0] * len(height);
        n = len(height);
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i-1]);
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1]);
        water = 0;
        for i in range(0, n):
            h = min(maxRight[i], maxLeft[i]);
            if (h >= height[i]):
                water = water + abs(height[i]-h);
        return water;

sol = Solution();
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
print();