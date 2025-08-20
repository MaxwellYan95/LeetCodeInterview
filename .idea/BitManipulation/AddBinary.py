def addBinary(a: str, b: str) -> str:
    sum = ""
    longerStr = ""
    shorterStr = ""
    if (len(a) > len(b)):
        longerStr = a;
        shorterStr = b;
    else:
        longerStr = b;
        shorterStr = a;
    while len(longerStr) != len(shorterStr):
        shorterStr = ("0" + shorterStr)
    longerBits = list(longerStr)
    shorterBits = list(shorterStr)
    carry = 0
    for index in reversed(range(len(longerBits))):
        if (longerBits[index] == '1' and shorterBits[index] == '1' and carry == 1):
            sum = ("1" + sum)
            carry = 1
        elif (longerBits[index] == '1' and shorterBits[index] == '1' and carry == 0):
            sum = ("0" + sum)
            carry = 1
        elif ((longerBits[index] == '0' and shorterBits[index] == '1' and carry == 0)
              or (longerBits[index] == '1' and shorterBits[index] == '0' and carry == 0)):
            sum = ("1" + sum)
            carry = 0
        elif ((longerBits[index] == '0' and shorterBits[index] == '1' and carry == 1)
              or (longerBits[index] == '1' and shorterBits[index] == '0' and carry == 1)):
            sum = ("0" + sum)
            carry = 1
        else:
            sum = ("0" + sum)
            carry = 0
    if carry == 1:
        sum = ("1" + sum)
    return sum

print(addBinary("1010", "1011"))