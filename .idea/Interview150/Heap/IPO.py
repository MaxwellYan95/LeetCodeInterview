import heapq;


class Solution:
    # IMPORTANT NOTE
    # ===============
    # The problem never mentioned anything about the order of an array.
    # The problem said to pick k projects from the list such that you
    # make the maximum profit. You start off with w capital.
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        stack = [];
        n = len(profits);
        tupList = [(capital[i], profits[i]) for i in range(n)];
        tupList.sort();
        index = 0;
        heapq.heapify(stack);
        for _ in range(k):
            # Order of the "and" condition in a while loop matters
            while index < n and w >= tupList[index][0]:
                heapq.heappush(stack, -tupList[index][1]);
                index += 1;
            if not stack:
                break;
            w -= heapq.heappop(stack);
        return w;




sol = Solution();
print(sol.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]));
print();