class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left;
        leftBits = self.convertToBits(left);
        rightBits = self.convertToBits(right);
        place = 31;
        for index in range(len(leftBits)):
            if (leftBits[index] == 1 and rightBits[index] == 1):
                result = 2**place;
                index = index + 1;
                place = place - 1;
                while (leftBits[index] == rightBits[index]):
                    if leftBits[index] == 1:
                        result = result + 2**place;
                    index = index + 1;
                    place = place - 1;
                return result;
            elif (leftBits[index] == 1 or rightBits[index] == 1):
                break;
            place = place - 1;
        return 0;

    def convertToBits(self, num: int) -> list[int]:
        temp = num;
        bits = [];
        for place in range(31, -1, -1):
            if 2**place <= temp:
                bits.append(1);
                temp = temp - 2**place;
            else:
                bits.append(0);
        return bits;