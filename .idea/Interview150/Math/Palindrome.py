def isPalindrome(x: int) -> bool:
    if (x < 0):
        return False
    digits = []
    tempX = x
    while tempX != 0:
        digits.append(tempX % 10)
        tempX = (tempX // 10)
    palin = 0
    place = 10**(len(digits)-1)
    for d in digits:
        palin += (place * d)
        place = place // 10
    if (palin == x):
        return True
    else:
        return False

print(isPalindrome(10))