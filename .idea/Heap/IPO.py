import collections


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        stack = collections.deque();
        curW = w;
        curK = 0;
        maximum = 0;
        for index in range(len(profits)):
            curProfit = profits[index];
            capRequire = capital[index];
            if curK == k:
                freeUp = collections.pop();
                curW -= freeUp;
                curK -= 1;
                while curW >= capRequire:
                    freeUp = collections.pop();
                    curW -= freeUp;
                    curK -= 1;
                stack.append(freeUp);
                curW += freeUp;
                curK += 1;
            if curW >= capRequire:
                stack.append(curProfit);
                curW += curProfit;
                curK += 1;
                maximum = max(curW, maximum);
        return maximum;



sol = Solution();
print(sol.findMaximizedCapital(1, 2, [1, 2, 3], [1, 1, 2]));
print();