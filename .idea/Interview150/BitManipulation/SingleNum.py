def singleNumber(self, nums: List[int]) -> int:
    dictNum = {n: nums.count(n) for n in set(nums)}
    for num in dictNum.keys():
        if (dictNum[num] == 1):
            return num