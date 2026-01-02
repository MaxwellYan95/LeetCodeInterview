class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums];
        elif len(nums) == 2:
            return [nums, nums[::-1]];
        else:
            result = [];
            leftVal = nums[0]
            leftLst = self.permute(nums[1:]);
            rightVal = nums[len(nums)-1]
            rightLst = self.permute(nums[:len(nums)-1]);
            for lst in leftLst:
                lst1 = lst.copy();
                lst1.append(leftVal);
                if lst1 not in result:
                    result.append(lst1);
                lst2 = lst.copy();
                lst2.insert(0, leftVal);
                if lst2 not in result:
                    result.append(lst2);
            for lst in rightLst:
                lst1 = lst.copy();
                lst1.append(rightVal);
                if lst1 not in result:
                    result.append(lst1);
                lst2 = lst.copy();
                lst2.insert(0, rightVal);
                if lst2 not in result:
                    result.append(lst2);
            return result;

sol = Solution();
print(sol.permute([1,2,3,4]))