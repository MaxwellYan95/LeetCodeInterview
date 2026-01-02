import collections;

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        def dfs(x: int, y: int):
            if (x < 0 or y < 0 or x >= len(board[0]) or y >= len(board) or board[y][x] != "O"):
                return;
            board[y][x] = "#";
            dfs(x-1, y);
            dfs(x+1, y);
            dfs(x, y-1);
            dfs(x, y+1);

        for y in range(len(board)):
            hasO = (board[y][0] == "O");
            if hasO:
                dfs(0, y);
            hasO = (board[y][len(board[0])-1] == "O");
            if hasO:
                dfs(len(board[0])-1, y);

        for x in range(len(board[0])):
            hasO = (board[0][x] == "O");
            if hasO:
                dfs(x, 0);
            hasO = (board[len(board)-1][x] == "O");
            if hasO:
                dfs(x, len(board)-1);

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "#":
                    board[y][x] = "O";
                else:
                    board[y][x] = "X";



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