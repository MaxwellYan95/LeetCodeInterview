import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.insert(0, -(math.inf-1));
        nums2.insert(0, -(math.inf-1));
        nums1.append(math.inf)
        nums2.append(math.inf)
        i1 = (len(nums1)-1)//2;
        i2 = (len(nums2)-1)//2;
        if (len(nums1) == len(nums2)):
            i2 = i2 - 1;
        while i1 < len(nums1)-1 or i2 < len(nums2)-1 or i1 > 0 or i2 > 0:
            left1 = nums1[i1];
            right1 = nums1[i1+1];
            left2 = nums2[i2];
            right2 = nums2[i2+1];
            print(f"nums1 = {nums1}");
            print(f"nums2 = {nums2}");
            print(f"l1 = {left1}, r1 = {right1}, l2 = {left2}, r2 = {right2}");
            if right2 < left1:
                i2 = i2 + 1;
                i1 = i1 - 1;
            elif left2 > right1:
                i2 = i2 - 1;
                i1 = i1 + 1;
            else:
                break;
        if (len(nums1)+len(nums2)) % 2 == 0:
            return (min(right1, right2)+max(left1, left2)) / 2
        return max(left1, left2);

sol = Solution();
print(sol.findMedianSortedArrays([1, 3, 4], [2, 5]));
print("")
print(sol.findMedianSortedArrays([1, 2, 3], [4, 5]));
print("")

print(sol.findMedianSortedArrays([1], []));
print("")
print(sol.findMedianSortedArrays([1], [1]));
print("")
print(sol.findMedianSortedArrays([1], [2, 3, 4]));
print("")