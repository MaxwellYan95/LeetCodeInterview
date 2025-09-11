import heapq;
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        minH = [];
        results = [];
        heapq.heapify(minH);
        index1 = 0;
        index2 = 0;
        heapq.heappush(minH, [nums1[index1]+nums2[index2], index1, index2])
        visited = set();
        visited.add((0,0));
        counter = 0;
        while counter != k:
            addedVal, i1, i2 = heapq.heappop(minH);
            results.append((nums1[i1], nums2[i2]));
            if i1+1 < len(nums1) and (i1+1, i2) not in visited:
                heapq.heappush(minH, [nums1[i1+1]+nums2[i2], i1+1, i2])
                visited.append((i1+1, i2))
            if i2+1 < len(nums2) and (i1, i2+1) not in visited:
                heapq.heappush(minH, [nums1[i1]+nums2[i2+1], i1, i2+1])
                visited.append((i1, i2+1))
            counter += 1;
        return results;

sol = Solution();
print(sol.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 20));