import collections
import heapq


class Solution:
    def gridToLine(self, board: list[list[int]]) -> list[int]:
        forward = True;
        line = [];
        for b in reversed(board):
            if forward:
                line.extend(b);
            else:
                line.extend(reversed(b));
        return line;


    def snakesAndLadders(self, board: list[list[int]]) -> int:
        line = self.gridToLine(board);
        bestSpot = [];
        heapq.heapify(bestSpot);
        def bfs(spot: int):
            moves = -1;
            if spot == len(line):
                return 0;
            endBound = min(spot+6, len(line)-1);
            endSpot = line[endBound];
            for next in line[spot+1: endBound-1]:
                if next != -1:
                    heapq.heappush(bestSpot, -next);
            if endSpot == -1:
                heapq.heappush(bestSpot, -endBound);
            else:
                heapq.heappush(bestSpot, -endSpot);
            while bestSpot:
                nextSpot = -heapq.heappop(bestSpot);
                if moves == -1:
                    moves = 1+bfs(nextSpot);
                else:
                    moves = min(moves, 1);
            return moves;
        return bfs(0);


sol = Solution();
print(sol.gridToLine([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))