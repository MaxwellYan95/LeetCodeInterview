class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapping = {}
        keys = [];
        for index in range(len(fruits)):
            oneFruit = fruits[index]
            if oneFruit not in mapping:
                mapping[oneFruit] = index;
                keys.append(oneFruit);
        keys.append(len(fruits));
        mapping[len(fruits)] = len(fruits);
        maximum = mapping[keys[2]] - mapping[keys[0]];
        for index in range(2, len(keys)):
            lowVal = mapping[keys[index-2]]
            highVal = mapping[keys[index]]
            maximum = max(maximum, highVal-lowVal);
        return maximum