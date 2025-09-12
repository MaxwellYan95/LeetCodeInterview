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
                insideLoop = False;
                while curW > capRequire and stack:
                    insideLoop = True;
                    freeUp = stack.pop();
                    curW -= freeUp;
                    curK -= 1;
                if insideLoop and curW < capRequire:
                    stack.append(freeUp);
                    curW += freeUp;
                    curK += 1;
            if curW >= capRequire and curK < k:
                stack.append(curProfit);
                curW += curProfit;
                curK += 1;
                maximum = max(curW, maximum);
        return maximum;



sol = Solution();
print(sol.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]));
print();