import heapq;
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        minH = []
        heapq.heapify(minH)
        heapq.heappush(minH, [nums1[0]+nums2[0], (0, 0)]);
        results = []
        visited = set();
        visited.add((0,0))
        while len(minH) != 0 and len(results) != k:
            total, indices = heapq.heappop(minH);
            i1 = indices[0];
            i2 = indices[1];
            results.append([nums1[i1], nums2[i2]]);
            if i1+1 < len(nums1) and (i1+1, i2) not in visited:
                heapq.heappush(minH, [nums1[i1+1]+nums2[i2], (i1+1, i2)]);
                visited.add((i1+1, i2))
            if i2+1 < len(nums2) and (i1, i2+1) not in visited:
                heapq.heappush(minH, [nums1[i1]+nums2[i2+1], (i1, i2+1)]);
                visited.add((i1, i2+1))
        return results




sol = Solution();
lst = [[1,1]];
print([1,1] not in lst);
print(sol.kSmallestPairs([1,7,11], [2,4,6], 7));