def singleNumber(self, nums: List[int]) -> int:
    numSorted = sorted(nums)
    for index in range(0, len(nums), 3):
        numSet = set(numSorted[index: index+3])
        if (len(numSet) != 1):
            numsThree = numSorted[index: index+3]
            numsThreeDict = {val: numsThree.count(val) for val in set(numsThree)}
            for val, count in numsThreeDict.items():
                if count == 1:
                    return val
    return numSorted[len(nums)-1]