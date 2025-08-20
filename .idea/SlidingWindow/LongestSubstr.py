def lengthOfLongestSubstring(s: str) -> int:
    sList = list(s)
    longest = ""
    lengths = []
    for char in sList:
        if char in list(longest):
            lengths.append(len(longest))
            ind = list(longest).index(char)
            longest = "".join(list(longest)[ind+1: len(longest)])
        longest = ("" + longest + str(char))
    lengths.append(len(longest))
    return sorted(lengths, reverse=True)[0]

print(lengthOfLongestSubstring("abcabcc"))