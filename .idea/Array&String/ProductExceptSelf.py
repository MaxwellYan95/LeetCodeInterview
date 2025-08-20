def productExceptSelf(nums: list[int]) -> list[int]:
    answer = [1] * len(nums)
    numSet = set(nums)
    numDict = {n: list.count(nums, n) for n in numSet}
    for index in range(len(answer)):
        numDict[nums[index]] = numDict[nums[index]]-1
        for key, value in numDict.items():
            answer[index] = answer[index] * key**value
        numDict[nums[index]] = numDict[nums[index]]+1
    return answer

n = [1,2,3,4]
print(productExceptSelf(n))