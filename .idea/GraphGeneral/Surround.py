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
        def dfs(x: int, y: int, edge: bool) -> bool:
            condList = [];
            onEdge = (x == 0 or x == len(board[0])-1 or y == 0 or y == len(board)-1);
            adj = self.adjacent(x, y, len(board[0])-1, len(board)-1);
            visited[y][x] = "X";
            for x1, y1 in adj:
                hasO = (board[y1][x1] == "O")
                notVisited = (visited[y1][x1] != "X");
                if hasO and notVisited:
                    condList.append(dfs(x1, y1, onEdge));
            if False not in condList and edge != True and onEdge != True:
                for x1, y1 in adj:
                    board[y1][x1] = "X";
                return True;
            return False;
        for y in range(len(board)):
            for x in range(len(board[y])):
                hasO = (board[y][x] == "O")
                notVisited = (visited[y][x] != "X");
                if hasO and notVisited:
                    dfs(x, y, False);
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