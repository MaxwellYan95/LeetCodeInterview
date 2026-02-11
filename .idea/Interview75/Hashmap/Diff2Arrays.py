class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        inNum1 = set();
        inNum2 = set();
        for n1 in nums1:
            if n1 not in nums2:
                inNum1.add(n1)
        for n2 in nums2:
            if n2 not in nums1:
                inNum2.add(n2)
        return [list(inNum1), list(inNum2)]