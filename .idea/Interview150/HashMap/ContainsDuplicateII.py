class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictIndex = {};
        for index in range(len(nums)):
            element = nums[index];
            if element not in dictIndex.keys():
                dictIndex[element] = [index];
            else:
                dictIndex[element].append(index);
        for key in dictIndex.keys():
            lst = dictIndex[key];
            for index in range(len(lst)-1):
                diff = abs(lst[index] - lst[index+1]);
                if (diff <= k):
                    return True;
        return False;