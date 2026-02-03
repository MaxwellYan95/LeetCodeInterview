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
    dp[m-1][n-1] = grid[m-1][n-1] # forget about "dp[m-1][n-1] = grid[m-1][n-1]"
    for index in range(n-2, -1, -1):
        dp[m-1][index] = grid[m-1][index] + dp[m-1][index+1]
    for index in range(m-2, -1, -1):
        dp[index][n-1] = grid[index][n-1] + dp[index+1][n-1]
    for curN in range(n-2, -1, -1):
        for curM in range(m-2, -1, -1):
            dp[curM][curN] = grid[curM][curN] + min(dp[curM+1][curN], dp[curM][curN+1])
    return dp[0][0]

user_logic([[1,3,1], [1,5,1], [4,2,1]])