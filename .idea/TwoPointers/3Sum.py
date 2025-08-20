#def threeSum(self, nums: List[int]) -> List[List[int]]:
#    results = []
#    for first in range(0, len(nums)-2):
#        for second in range(first+1, len(nums)-1):
#            for third in range(second+1, len(nums)):
#                if (nums[first]+nums[second]+nums[third]) == 0:
#                    list = sorted([nums[first], nums[second], nums[third]])
#                    if list not in results:
#                        results.append(list)
#    return results

def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    max = sorted(nums)[len(nums)-1]
    min = sorted(nums)[0]
    negative = []
    positive = []
    if (abs(min) > max*2):
        negative = sorted([n for n in nums if n < 0 and n >= min/2])
        positive = sorted([n for n in nums if n >= 0], reverse=True)
    elif (max > abs(min*2)):
        negative = sorted([n for n in nums if n < 0])
        positive = sorted([n for n in nums if n >= 0 and n <= max/2], reverse=True)
    else:
        negative = sorted([n for n in nums if n < 0])
        positive = sorted([n for n in nums if n >= 0], reverse=True)
    sortedNums = sorted(negative + positive)
    for pos in positive:
        sortedNums.remove(pos)
        list = twoSum(sortedNums, -pos)
        for lst in list:
            if lst not in result:
                result.append(list)
    return result




def twoSum(numbers: list[int], target: int) -> list[list[int]]:
    results = []
    numSet = set(numbers)
    dict = {val:numbers.count(val) for val in numSet}
    keyList = list(dict.keys())
    for key in keyList:
        if (target%2 == 0 and key*2 == target and dict.get(key) > 1):
            results.append(sorted([-target, key, key]))
        desiredNum = target - key
        if desiredNum in keyList:
            results.append(sorted([-target, desiredNum, key]))
    return results

print(threeSum([-1, 0, 1, 2, -1, -4]))