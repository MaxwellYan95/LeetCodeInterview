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
                endBound = min(spot+7, len(line));
                forward = [spot+1, moves+1];
                forwardSpot = spot+1;
                for next in line[spot+1: endBound]:
                    if next != -1 and next != spot:
                        heapq.heappush(bestSpot, [-next, moves+1]);
                    else:
                        forward[0] = -forwardSpot;
                    forwardSpot += 1;
                heapq.heappush(bestSpot, forward);
        bfs();
        return self.minMoves;


sol = Solution();
print(sol.gridToLine([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))