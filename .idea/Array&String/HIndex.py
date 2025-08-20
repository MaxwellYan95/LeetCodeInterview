def hIndex(citations: list[int]) -> int:
    citations.sort(reverse=True)
    for index in range(len(citations)):
        indexPlus = index + 1
        value = citations[index]
        if value < indexPlus:
            return index
    return len(citations)

lst = [3, 0, 6, 1, 5]
print(hIndex(lst))