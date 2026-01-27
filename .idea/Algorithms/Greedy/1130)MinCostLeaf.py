import heapq


class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        stack = [(num, num, 1) for num in arr]

        heapq.heapify(stack)
        nonLeaf = 0;
        while len(stack) >= 2:
            tup1 = heapq.heappop(stack);
            min1 = max(tup1[1], tup1[2]);
            tup2 = heapq.heappop(stack);
            min2 = max(tup2[1], tup2[2]);
            nonLeaf += (min2*min1);
            heapq.heappush(stack, (min2*min1, min1, min2));
        return nonLeaf;

sol = Solution();
print(sol.mctFromLeafValues([7, 12, 8, 10]))


