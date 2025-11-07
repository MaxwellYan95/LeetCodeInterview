import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i1 = (len(nums1))//2
        i2 = (len(nums2))//2
        left1 = -(math.inf-1);
        right1 = math.inf;
        left2 = -(math.inf-1);
        right2 = math.inf;
        inBounds = True;
        while True:
            left1 = nums1[i1];
            right1 = nums1[i1+1];
            left2 = nums2[i2];
            right2 = nums2[i2+1];
            if right2 < left1:
                i2 = i2 + 1;
                i1 = i1 - 1;
            elif left2 > right1:
                i2 = i2 - 1;
                i1 = i1 + 1;
            else:
                break;
        if (len(nums1)+len(nums2)) % 2 == 0:
            return (min(right1, right2) + max(left1, left2)) / 2
        return max(left1, left2);

sol = Solution();
print(sol.findMedianSortedArrays([1, 3, 4], [2, 5]));
print(sol.findMedianSortedArrays([1, 2, 3], [4, 5]));

print(sol.findMedianSortedArrays([1], []));