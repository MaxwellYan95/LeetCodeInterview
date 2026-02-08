class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        height = [0];
        tallest = 0
        for index in range(len(gain)):
            g = gain[index]
            newH = g + height[index];
            height.append(newH);
            tallest = max(tallest, newH)
        return tallest