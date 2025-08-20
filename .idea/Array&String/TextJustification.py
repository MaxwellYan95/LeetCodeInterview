def multiWordSpacing(words: list[str], maxWidth: int) -> str:
    totalLength = 0
    for w in words:
        totalLength += len(w)
    spaces = (maxWidth - totalLength) // (len(words)-1)
    spacesRemain = (maxWidth - totalLength) % (len(words)-1)
    result = ""
    for w in words[0:len(words)-1]:
        numSpaces = spaces
        if (spacesRemain != 0):
            numSpaces = numSpaces + 1
            spacesRemain = spacesRemain - 1
        result += (w + "")
        for space in range(numSpaces):
            result += " "
    result += (words[len(words)-1] + "")
    return result

def spacing(words: list[str], maxWidth: int) -> str:
    result = ""
    if len(words) == 1:
        result += (words[0] + "")
        for space in range(maxWidth-len(words[0])):
            result += " "
    else:
        result += (multiWordSpacing(words, maxWidth))
    return result

def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    subList = []
    startInd = 0
    index = 0
    totalLen = 0
    result = ""
    while True:
        if (index == len(words)):
            subList = words[startInd: index]
            result += (spacing(subList, maxWidth) + "\n")
            break
        elif (totalLen + len(words[index]) > maxWidth):
            subList = words[startInd: index]
            result += (spacing(subList, maxWidth) + "\n")
            startInd = index
            totalLen = 0
        else:
            totalLen = totalLen + len(words[index]) + 1
            index = index + 1
    return result;

print(fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))