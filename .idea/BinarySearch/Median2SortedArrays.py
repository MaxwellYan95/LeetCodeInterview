import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A=nums1
        B=nums2

        if len(B)<len(A):
            A,B=B,A

        total=len(A)+len(B)
        half=total//2

        l=0
        r=len(A)-1

        while True:
            a=(r+l)//2
            b=half-a-2
            Aleft=A[a]   if a>=0 else float("-inf")
            Aright=A[a+1] if (a+1)<len(A) else float("inf")
            Bleft=B[b] if b>=0 else float("-inf")
            Bright=B[b+1] if (b+1)< len(B) else float("inf")

            if Aleft <= Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+ min(Aright,Bright))/2

            elif Aleft>Bright:
                r=a-1

            else:
                l=a+1

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