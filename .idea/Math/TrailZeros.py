def trailingZeroes(n: int) -> int:
    fact = 1
    for num in range(1, n+1):
        fact *= num
    result = 0
    divisible = True
    while divisible == True:
        if fact % 10 == 0:
            fact = fact // 10
            result += 1
        else:
            divisible = False
    return result