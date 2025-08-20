def reverseBits(n: int) -> int:
    bitList = list(str(n));
    bitList.reverse();
    value = 0;
    place = 31;
    for bit in bitList:
        if bit == '1':
            value += 2**place;
        place -= 1;
    return value;

print();
