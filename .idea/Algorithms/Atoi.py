def myAtoi(self, s: str) -> int:
    digits = self.getDigits(s);
    place = 10 ** (len(digits)-2);
    sign = 1;
    if (len(digits) == 0):
        return 0;
    if (digits[0] == '-'):
        sign = -1;
    sum = 0;
    for d in digits[1:]:
        sum += int(d)*place;
        place = place // 10;
    sum *= sign;
    if (sum < -(2**31)):
        return -(2**31)
    elif (sum > 2**31-1):
        return 2**31-1
    return sum

def getDigits(self, s: str) -> list[str]:
    s = s.strip();
    lst = [];
    starts = False;
    for char in s:
        if starts:
            if not self.isDigit(char):
                break;
            else:
                lst.append(char)
        else:
            if (char == '-'):
                lst.append('-');
                starts = True;
            elif (char == '+'):
                lst.append('+');
                starts = True;
            elif (self.isDigit(char)):
                lst.append('+');
                lst.append(char);
                starts = True;
            elif (char != ' '):
                break;
    return lst;


def isDigit(self, s: str) -> bool:
    return s == '0' or s == '1' or s == '2' or s == '3' \
           or s == '4' or s == '5' or s == '6' or s == '7' \
           or s == '8' or s == '9'

def isSign(self, s: str) -> bool:
    return s == '+' or s == '-'
