class Solution:

    def maxArea(self, height: list[int]) -> int:
        p1 = 0;
        p2 = len(height)-1;
        area = 0;
        while p1 < p2:
            newArea = (p2-p1)*(min(height[p1], height[p2]));
            area = max(area, newArea);
            if height[p1] < height[p2]:
                p1 = p1+1;
            else:
                p2 = p2-1;
        return area;


