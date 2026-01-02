def plusOne(digits: list[int]) -> list[int]:
    digitPlus = 0
    place = 10**(len(digits)-1)
    for d in digits:
        digitPlus += (d * place)
        place = place // 10
    digitPlus += 1
    results = []
    while digitPlus != 0:
        d = digitPlus % 10
        results.append(d)
        digitPlus = digitPlus // 10
    return results[::-1]
print(plusOne([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]))