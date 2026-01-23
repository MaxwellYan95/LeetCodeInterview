class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def recur(nums: list[int], place: int):
            if len(nums) == 1:
                return nums;
            mapping = defaultdict(list)
            result = []
            keyLst = set();
            for n in nums:
                curKey = n
                for i in range(place):
                    curKey = curKey % 10;
                    mapping[curKey].append(n);
                    keyLst.add(curKey);
            for k in keyLst:
                result.extend(mapping[k], place+1);
