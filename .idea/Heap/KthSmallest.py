class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        index1 = 0;
        index2 = 0;
        if k == 0:
            return [[]]
        pairs = [[nums1[index1], nums2[index2]]];
        counter = 1;
        while True:
            if counter == k:
                break;

            if nums1[index1+1]+nums2[index2] < nums1[index1]+nums2[index2+1]:
                pairs.append([nums1[index1+1], nums2[index2]]);
                index1 = index1 + 1;
            else:
                pairs.append([nums1[index1], nums2[index2+1]]);
                index2 = index2 + 1;
            if index1 == len(nums1)-1:
                index1 = 0;
                index2 = index2 + 1;
            if index2 == len(nums2)-1:
                index2 = 0;
                index1 = index1 + 1;
        counter = counter + 1;
        return pairs;

sol = Solution();
print(sol.kSmallestPairs([1,7,11], [2,4,6], 7));