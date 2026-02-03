def user_logic(grid):
    """
    Write your logic here.
    Parameters:
        grid (list of list of int): The matrix of integers
    Returns:
        int: Computed result based on the problem statement
    """

    m = len(grid)
    n = len(grid[0])
    dp = [[-1 for i in range(n)] for j in range(m)]
    dp[m-1][n-1] = grid[m-1][n-1]
    index = [m-2, n-2]
    def recur(curM: int, curN: int):
        if dp[curM][curN] != -1:
            return dp[curM][curN]
        prevMin = float('inf')
        right = None;
        down = None;
        if curM+1 < m:
            prevMin = min(prevMin, recur(curM+1, curN))
        if curN+1 < n:
            prevMin = min(prevMin, recur(curM, curN+1))
        dp[curM][curN] = grid[curM][curN] + prevMin
        return dp[curM][curN]
    return recur(0, 0)