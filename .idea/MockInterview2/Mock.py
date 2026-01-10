class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # 0 is x and 1 is y
        intersect = [False, False];

        for index in range(len(rec1)):
            x_or_y = index % 2;
            curP = rec1[index]
            p2 = rec2[(index + 2) % 4];
            p1 = rec2[index];
            if p2 < curP < p1:
                intersect[x_or_y] = True;
            if p1 < curP < p2:
                intersect[x_or_y] = True;
            if False not in intersect:
                break;

        return intersect[0] and intersect[1];

    def partitionLabels(self, s: str) -> list[int]:
        letters = [];
        mapping = dict();
        for index in range(len(s)):
            char = s[index]
            if char not in letters:
                letters.append(char)
                mapping[char] = [index];
            else:
                mapping[char].append(index);
        minimum = mapping[letters[0]][0]
        maximum = mapping[letters[0]][len(mapping[letters[0]])-1];
        result = [];
        inIf = False;
        for char in letters[1:]:
            temp = mapping[char][0]
            if minimum <= temp <= maximum:
                minimum = min(minimum,
                              mapping[char][0])
                maximum = max(maximum,
                              mapping[char][len(mapping[char])-1])
                inIf = True;
            else:
                result.append(len(s[minimum: maximum+1]))
                if len(result) == 1:
                    minimum = mapping[char][0]
                    maximum = mapping[char][0] + 1;
                else:
                    minimum = mapping[char][0]
                    maximum = mapping[char][len(mapping[char])-1];
                inIf = False;
        if inIf:
            result.append(len(s[minimum:maximum+1]))
        return result





sol = Solution();
val = sol.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1])
print(sol.partitionLabels("eaaaabaaec"))