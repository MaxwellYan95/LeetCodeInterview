import heapq;
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        minH = [[nums2[0]+nums1[0], (0, 0)]]
        visited = set()
        results = []
        visited.add((0, 0))
        heapq.heapify(minH)
        while len(results) != k:
            total, coord = heapq.heappop(minH)
            i1 = coord[0]
            i2 = coord[1]
            results.append([nums1[i1], nums2[i2]])
            bounds1 = (i1+1) < len(nums1)
            bounds2 = (i2+1) < len(nums2)
            if (i1+1, i2) not in visited and bounds1:
                heapq.heappush(minH, [nums2[i2]+nums1[i1+1], (i1+1, i2)])
                visited.add((i1+1, i2))
            if (i1, i2+1) not in visited and bounds2:
                heapq.heappush(minH, [nums2[i2+1]+nums1[i1], (i1, i2+1)])
                visited.add((i1, i2+1))
        return results



sol = Solution();
lst = [[1,1]];
print([1,1] not in lst);
print(sol.kSmallestPairs([1,7,11], [2,4,6], 7));