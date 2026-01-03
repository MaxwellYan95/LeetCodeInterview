class Solution:
    def candy(self, ratings: list[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)*1;
        left = 0;
        right = len(ratings)-1;
        candies = [1]*len(ratings);
        while left < len(ratings)-1:
            if ratings[left] < ratings[left+1]:
                candies[left+1] = candies[left] + 1;
            left += 1
        while right > 0:
            notGreater = not (candies[right] < candies[right-1])
            if ratings[right] < ratings[right-1] and notGreater:
                candies[right-1] = candies[right] + 1;
            right -= 1;
        return sum(candies);

sol = Solution()
print(sol.candy([1, 3, 4, 5, 2]))