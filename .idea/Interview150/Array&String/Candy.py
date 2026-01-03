class Solution:
    def candy(self, ratings: list[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)*1;
        leftRate = ratings[0];
        rightRate = ratings[len(ratings)-1]
        candies = 0;
        if (leftRate > ratings[1]):
            candies += 2;
        else:
            candies += 1;
        if (rightRate > ratings[len(ratings)-2]):
            candies += 2;
        else:
            candies += 1;
        for index in range(0, len(ratings)):
            if index == 0:
                if ratings[index] > ratings[index+1]:
                    candies += 2;
                else:
                    candies += 1;
                continue
            elif index == len(ratings)-1:
                if ratings[index] > ratings[index-1]:
                    candies += 2;
                else:
                    candies += 1;
                continue
            equal = (ratings[index] >= ratings[index-1] and ratings[index] >= ratings[index+1]);
            greater = (ratings[index] > ratings[index-1] or ratings[index] > ratings[index+1])
            if greater and equal:
                candies += 2;
            else:
                candies += 1;
        return candies;

sol = Solution()
print(sol.candy())