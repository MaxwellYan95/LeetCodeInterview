import collections
import heapq


class Solution:
    def gridToLine(self, board: list[list[int]]) -> list[int]:
        forward = True;
        # Add extra element to make sure indices are aligned
        line = [-1];
        for b in reversed(board):
            if forward:
                line.extend(b);
                # I forgot to change the forward variable
                forward = False;
            else:
                line.extend(reversed(b));
                forward = True;
        return line;


    def snakesAndLadders(self, board: list[list[int]]) -> int:
        line = self.gridToLine(board);
        stack = collections.deque();
        visited = [False for i in line];
        visited[1] = True;
        stack.append([1, 0]);
        final = len(line)-1;
        self.minMoves = -1;
        while stack:
            # Look at the possible moves you can make
            spot, moves = stack.popleft();
            for dice in range(1, 7):
                next = spot + dice;
                if next > final:
                    continue;
                if line[next] != -1:
                    next = line[next];
                if next == final:
                    if self.minMoves == -1:
                        self.minMoves = moves+1;
                    else:
                        self.minMoves = min(self.minMoves, moves+1);
                if visited[next] == False:
                    visited[next] = True;
                    stack.append([next, moves+1]);
        return self.minMoves;



sol = Solution();
print(sol.gridToLine([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(sol.snakesAndLadders([[-1,4,-1],[6,2,6],[-1,3,-1]]))
print(sol.snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))