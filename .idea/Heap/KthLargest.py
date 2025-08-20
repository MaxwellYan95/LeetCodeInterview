class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        sortedNums = self.mergeSort(nums);
        return sortedNums[k-1];

    def mergeSort(self, nums: list[int]) -> list[int]:
        if len(nums) == 0:
            return [];
        elif len(nums) == 1:
            return [nums[0]];
        else:
            leftLst = self.mergeSort(nums[:int(len(nums)/2)]);
            rightLst = self.mergeSort(nums[int(len(nums)/2):]);
            leftIndex = 0;
            rightIndex = 0;
            result = [];
            while not(leftIndex == len(leftLst) and rightIndex == len(rightLst)):
                if leftIndex == len(leftLst):
                    result.append(rightLst[rightIndex]);
                    rightIndex += 1;
                elif rightIndex == len(rightLst):
                    result.append(leftLst[leftIndex]);
                    leftIndex += 1;
                else:
                    leftNum = leftLst[leftIndex];
                    rightNum = rightLst[rightIndex];
                    if (rightNum > leftNum):
                        result.append(rightNum);
                        rightIndex += 1;
                    else:
                        result.append(leftNum);
                        leftIndex += 1;
            return result;



sol = Solution();
print(sol.findKthLargest([3,2,1,5,6,4], 2));
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4));
print(sol.findKthLargest([3,1,2,4], 2));
print();