from collections import defaultdict

class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1;
        if len(chars) == 1:
            return len(chars);
        index = 0;
        bound = 0;
        while index < len(chars):
            c1 = chars[index]
            index += 1;
            count = 1;
            while index < len(chars) and c1 == chars[index]:
                index += 1;
                count += 1;
            count = str(count);
            chars[bound] = c1;
            bound += 1;
            if count != '1':
                for num in count:
                    chars[bound] = num;
                    bound += 1;
        chars = chars[:bound];
        return len(chars);

sol = Solution()
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]
                   ))
