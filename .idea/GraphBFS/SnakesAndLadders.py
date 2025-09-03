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
        heapq.heappush(bestSpot, [0, 0])
        self.minMoves = -1;
        def bfs():
            while bestSpot:
                spot, moves = heapq.heappop(bestSpot);
                spot = -spot;
                if spot == len(line)-1:
                    if self.minMoves == -1:
                        self.minMoves = moves;
                    else:
                        self.minMoves = min(self.minMoves, moves);
                    continue;
                endBound = min(spot+6, len(line)-1);
                endSpot = line[endBound];
                for next in line[spot+1: endBound-1]:
                    if next != -1:
                        heapq.heappush(bestSpot, [-next, moves+1]);
                if endSpot == -1:
                    heapq.heappush(bestSpot, [-endBound, moves+1]);
                else:
                    heapq.heappush(bestSpot, [-endSpot, moves+1]);
        bfs();
        return self.minMoves;


sol = Solution();
print(sol.gridToLine([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))