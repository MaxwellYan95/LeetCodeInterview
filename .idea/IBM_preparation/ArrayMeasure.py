def user_logic(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Number of elements in the array
        arr (list of int): List of integers
    Returns:
        int: Computed result based on the problem statement
    """
    sortArr = sorted(arr)
    sortIndex = {}
    for index in range(len(sortArr)):
        num = sortArr[index]
        sortIndex[num] = index;
    result = 0;
    for index in range(len(arr)):
        num = arr[index]
        result += (sortIndex[num] + index);
    return result