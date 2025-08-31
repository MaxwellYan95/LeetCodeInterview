import collections;

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
        visited = [["X" for inner in board[0]] for outer in board];
        stack = collections.deque();
        def bfs(startX: int, startY: int):
            stack.append([startX, startY]);
            while stack:
                x, y = stack.popleft();
                visited[y][x] = "O";
                adj = self.adjacent(x, y, len(board[0])-1, len(board)-1);
                for x1, y1 in adj:
                    hasO = (board[y1][x1] == "O")
                    notVisited = (visited[y1][x1] == "X");
                    if hasO and notVisited:
                        stack.append([x1, y1]);

        for y in range(len(board)):
            hasO = (board[y][0] == "O");
            notVisited = (visited[y][0] == "X");
            if hasO and notVisited:
                bfs(0, y);
            hasO = (board[y][len(board[0])-1] == "O");
            notVisited = (visited[y][len(board[0])-1] == "X");
            if hasO and notVisited:
                bfs(len(board[0])-1, y);

        for x in range(len(board[0])):
            hasO = (board[0][x] == "O");
            notVisited = (visited[0][x] == "X");
            if hasO and notVisited:
                bfs(x, 0);
            hasO = (board[len(board)-1][x] == "O");
            notVisited = (visited[len(board)-1][x] == "X");
            if hasO and notVisited:
                bfs(x, len(board)-1);

        for y in range(len(visited)):
            for x in range(len(visited[0])):
                board[y][x] = visited[y][x];



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