def max_books_on_shelf(heights: list[int]):
    """
    Write your logic here.
    Parameters:
        heights (list): List of integers representing the height of the books
    Returns:
        int: Maximum number of books that can be placed on the new shelf
    """
    dp = [1 for i in range(len(heights))];
    dp[0] = 1;
    maximum = 1;
    for index in range(1, len(heights)):
        n1 = heights[index]
        for inner in range(0, index):
            n2 = heights[inner]
            if n1 > n2:
                dp[index] = max(dp[index], dp[inner]+1);
                maximum = max(maximum, dp[index])
    return maximum

print(max_books_on_shelf([10, 9, 2, 5, 3, 7, 101, 18]))