def twoSum(numbers: list[int], target: int) -> list[int]:
    numSet = set(numbers)
    dict = {val:numbers.count(val) for val in numSet}
    keyList = list(dict.keys())
    for first in range(len(keyList)):
        firstVal = keyList[first]
        if (target%2 == 0 and firstVal*2 == target and dict.get(firstVal) > 1):
            return sorted([numbers.index(firstVal)+1, numbers.index(firstVal, numbers.index(firstVal)+1)+1])
        for second in range(first+1, len(keyList)):
            secondVal = keyList[second]
            if (firstVal + secondVal == target):
                return sorted([numbers.index(firstVal)+1, numbers.index(secondVal)+1])
    return [];

lst = list((0,0,3,4))
print(twoSum(lst, 0))



