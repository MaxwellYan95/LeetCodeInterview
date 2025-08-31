import collections

class Solution:
    def adjacent(self, x: int, y: int, maxX: int, maxY: int):
        adj = [];
        if (y != 0):
            adj.append([x, y-1]);
        if (y != maxY):
            adj.append([x, y+1]);
        if (x != 0):
            adj.append([x-1, y]);
        if (x != maxX):
            adj.append([x+1, y]);
        return adj;
    def solve(self, board: list[list[str]]) -> None:
        visited = [["0" for inner in board[0]] for outer in board];
        stack = collections.deque();
        def bfs(startX: int, startY: int):
            stack.append([startX, startY]);
            coordinates = [[startX, startY]];
            onEdge = False;
            while stack:
                x, y = stack.popleft();
                visited[y][x] = "X";
                adj = self.adjacent(x, y, len(board[0])-1, len(board)-1);
                if not onEdge:
                    onEdge = (x == 0 or x == len(board[0])-1 or y == 0 or y == len(board)-1);
                for x1, y1 in adj:
                    hasO = (board[y1][x1] == "O")
                    notVisited = (visited[y1][x1] != "X");
                    if hasO and notVisited:
                        coordinates.append([x1, y1]);
                        stack.append([x1, y1]);
            if not onEdge:
                for x, y in coordinates:
                    board[y][x] = "X";


        for y in range(len(board)):
            for x in range(len(board[y])):
                hasO = (board[y][x] == "O")
                notVisited = (visited[y][x] != "X");
                if hasO and notVisited:
                    bfs(x, y);
        return board;


sol = Solution();
print(sol.solve([["O","O","O","O","X","X"],
             ["O","O","O","O","O","O"],
             ["O","X","O","X","O","O"],
             ["O","X","O","O","X","O"],
             ["O","X","O","X","O","O"],
             ["O","X","O","O","O","O"]]))
print(sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
print(sol.solve([["X","X","X"],["X","O","X"],["X","X","X"]]));
print(sol.solve([["O","O","O","O","X","X"],
                 ["O","O","O","O","O","O"],
                 ["O","X","O","X","O","O"],
                 ["O","X","O","O","X","O"],
                 ["O","X","O","X","O","O"],
                 ["O","X","O","O","O","O"]]))