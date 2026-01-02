class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            return nums1;
        index1 = m-1;
        index2 = n-1;
        ind = m+n-1;
        while (index2 >= 0 or index1 >= 0):
            if index1 < 0:
                nums1[ind] = nums2[index2];
                index2 -= 1;
            elif index2 < 0:
                nums1[ind] = nums1[index1];
                index1 -= 1;
            elif nums1[index1] > nums2[index2]:
                nums1[ind] = nums1[index1];
                index1 -= 1;
            else:
                nums1[ind] = nums2[index2];
                index2 -= 1;
            ind -= 1;

sol = Solution();
print(sol.merge([0], 0, [1], 1));

