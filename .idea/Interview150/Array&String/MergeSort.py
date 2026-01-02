class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if m == 0:
            return nums2[:n];
        if n == 0:
            return nums1[:m];
        index1 = 0;
        index2 = 0;
        ind = 0;
        n1 = nums1[:n];
        while (index2 < n or index1 < m):
            if (index1 == m):
                nums1[ind] = nums2[index2];
                index2 += 1;
            elif (index2 == n):
                nums1[ind] = n1[index1];
                index1 += 1;
            else:
                if n1[index1] >= nums2[index2]:
                    nums1[ind] = nums2[index2];
                    index2 += 1;
                else:
                    nums1[ind] = n1[index1];
                    index1 += 1;
            ind += 1;

sol = Solution();
print(sol.merge([0], 0, [1], 1));

