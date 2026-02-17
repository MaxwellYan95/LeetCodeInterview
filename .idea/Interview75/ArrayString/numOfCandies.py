class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandy = max(candies)
        result = [];
        for c in candies:
            if c + extraCandies >= maxCandy:
                result.append(True);
            else:
                result.append(False);
        return result