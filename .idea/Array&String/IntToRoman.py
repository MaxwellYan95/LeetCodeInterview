def intToRoman(num: int) -> str:
    symbol = {1000: "M",
              900: "CM",
              500: "D",
              400: "CD",
              100: "C",
              90: "XC",
              50: "L",
              40: "XL",
              10: "X",
              9: "IX",
              5: "V",
              4: "IV",
              1: "I"}
    keyList = list(symbol.keys())
    numTemp = num
    roman = ""
    while numTemp > 0:
        if numTemp >= keyList[0]:
            numTemp -= keyList[0]
            roman += symbol.get(keyList[0])
        else:
            keyList.pop(0)
    return roman

print(intToRoman(50))
