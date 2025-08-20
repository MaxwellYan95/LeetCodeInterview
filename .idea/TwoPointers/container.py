def maxArea(height: list[int]) -> int:
    small = 0;
    big = len(height)-1;
    area = 0;
    while big > small:
        area = max(area, (big - small) * min(height[small], height[big]))
        if (height[big] < height[small]):
            big = big - 1;
        else:
            small = small + 1;
    return area;

h = [1,8,6,2,5,4,8,3,7]
maxArea(h)


