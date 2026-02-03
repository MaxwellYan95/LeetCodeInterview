def max_books_on_shelf(heights: list[int]):
    """
    Write your logic here.
    Parameters:
        heights (list): List of integers representing the height of the books
    Returns:
        int: Maximum number of books that can be placed on the new shelf
    """
    dp = {};
    dp[heights[0]] = 1;
    maximum = 1;
    for index in range(1, len(heights)):
        num = heights[index]
        dp[num] = 1;
        keys = [k for k in dp]
        for k in keys:
            if num > k:
                dp[num] = max(dp[num], dp[k] + 1);
                maximum = max(maximum, dp[num])
    return maximum

print(max_books_on_shelf([10, 9, 2, 5, 3, 7, 101, 18]))