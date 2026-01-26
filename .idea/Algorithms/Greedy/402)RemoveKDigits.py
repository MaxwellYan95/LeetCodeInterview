from collections import defaultdict

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        place = len(num)
        keys = []
        mapping = {}
        for index in range(place):
            digit = int(num[index]);
            priority = digit / (index + 1);
            mapping[priority] = digit;
            keys.append(priority);
        keys.sort(reverse=True);
        for i in range(k):
            mapping.pop(keys[i]);
        return "".join(list(mapping.values()));