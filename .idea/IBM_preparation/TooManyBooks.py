def max_books_on_shelf(heights: list[int]):
    """
    Write your logic here.
    Parameters:
        heights (list): List of integers representing the height of the books
    Returns:
        int: Maximum number of books that can be placed on the new shelf
    """
    maximum = 0;
    for index in range(0, len(heights)-1):
        cur = heights[index]
        next = heights[index+1];
        if cur < next:
            maximum += 1;
    return maximum+1

print(max_books_on_shelf([10, 9, 2, 5, 3, 7, 101, 18]))