class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [];
        for index in range(len(ratings)):
            candies.append(1);
        for index in range(1, len(ratings)):
            if ratings[index-1] < ratings[index]:
                candies[index] = candies[index-1]+1;
        for index in range(len(ratings)-2, -1, -1):
            if ratings[index] > ratings[index+1]:
                candies[index] = max(candies[index], candies[index+1]+1);
        return sum(candies);

sol = Solution();
print(sol.candy([1,2,2]));
print(sol.candy([1,2,1]));
print(sol.candy([1,0,2]));
print(sol.candy([1, 2, 87, 87, 87, 2, 1]));