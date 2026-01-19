class Solution:

    def romanToInt(self, s: str) -> int:
        nums1 = [1, 5, 10, 50, 100, 500, 1000]
        self.symbols1 = ["I", "V", "X", "L", "C", "D", "M"]
        nums2 = [4, 9, 40, 90, 400, 900]
        self.symbols2 = ["IV", "IX", "XL", "XC", "CD", "CM"]
        self.romanMap = {};
        for i in range(len(nums1)):
            self.romanMap[self.symbols1[i]] = nums1[i];
        for i in range(len(nums2)):
            self.romanMap[self.symbols2[i]] = nums2[i];
        index = 0;
        s2 = s;
        result = 0;
        while index < len(s):
            two = s2[index: index+2]
            one = s2[index];
            if two in self.symbols2:
                result += self.romanMap[two];
                index += 2;
            else:
                result += self.romanMap[one];
                index += 1;
        return result;


    def romanNum(self, s: str):
        romanMap = {};
        nums1 = [1, 5, 10, 50, 100, 500, 1000]
        symbols1 = ["I", "V", "X", "L", "C", "D", "M"]
        nums2 = [4, 9, 40, 90, 400, 900]
        symbols2 = ["IV", "IX", "XL", "XC", "CD", "CM"]
        for i in range(len(nums1)):
            romanMap[symbols1[i]] = nums1[i];
        for i in range(len(nums2)):
            romanMap[symbols2[i]] = nums2[i];
        return romanMap[s];


