class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

    def shortenArray(self, nums: list[int]) -> list[int]:
        sumCounter = 0;
        negativeOrZero = False;
        leftIndex = 0;
        rightIndex = len(nums);
        for index in range(len(nums)):
            n = nums[index];
            sumCounter += n;
            if sumCounter <= 0 and negativeOrZero == False:
                negativeOrZero = True;
            if n > 0 and negativeOrZero == True:
                leftIndex = index;
                break;
        sumCounter = 0;
        negativeOrZero = False;
        for index in range(len(nums)-1, -1, -1):
            n = nums[index];
            sumCounter += n;
            if sumCounter <= 0 and negativeOrZero == False:
                negativeOrZero = True;
            if n > 0 and negativeOrZero == True:
                rightIndex = index+1;
                break;
        return nums[leftIndex: rightIndex];


sol = Solution();
print(sol.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]));
