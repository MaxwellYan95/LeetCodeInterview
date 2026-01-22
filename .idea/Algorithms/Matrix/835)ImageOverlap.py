from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)

        coord1 = []
        coord2 = []
        transformations = defaultdict(int)

        # Filter points having 1 for each matrix respectively.
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    coord1.append((i, j))
                if img2[i][j] == 1:
                    coord2.append((i, j))

        # For every point in filtered A, calculate the
        # linear transformation vector with all points of filtered B
        # count the number of the pairs that have the same transformation vector
        for c1 in coord1:
            for c2 in coord2:
                transformations[(c1[0]-c2[0], c1[1]-c2[1])] += 1;
        if (len(transformations.values()) == 0):
            return 0;
        return sorted(transformations.values())[len(transformations.values())-1];