class Solution:
    output: int = 0
    def dfs(self, row: int, n: int, placed: list[tuple[int, int]]) -> None:
        # row == n means that all n queens are placed
        # each queen must be in a unique row
        if row == n:
            self.output += 1
            return
        # looks at every possible column position
        for col in range(n):
            can_place: bool = True
            # looks at the coordinates of all queens that if placed
            for x, y in placed:
                # col == y indicates if (x, y) is in the same column as a coordinate in "placed"
                # (abs(col - y) == abs(row - x)) indicates if (x, y) is diagonal to a coordinate in "placed"
                if col == y or row == x or (abs(col - y) == abs(row - x)):
                    can_place = False
                    break
            if not can_place: continue
            placed.append((row, col))
            self.dfs(row + 1, n, placed) # row + 1 allows the code to look at every row
            placed.pop() # steps back

    def totalNQueens(self, n: int) -> int:
        self.output = 0
        placed: list[tuple[int, int]] = []
        self.dfs(0, n, placed)
        return self.output