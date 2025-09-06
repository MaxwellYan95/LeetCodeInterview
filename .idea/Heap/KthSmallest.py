import heapq;
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        h = [];
        result = [];
        kCounter = 0;
        visited = [];
        heapq.heapify(h);
        heapq.heappush(h, [nums1[0]+nums2[0], 0, 0]);
        while kCounter < k and h:
            sum, i, j = heapq.heappop(h);
            result.append([nums1[i], nums2[j]]);
            visited.append([i, j]);
            if i+1 < len(nums1) and [i+1, j] not in visited:
                heapq.heappush(h, [nums1[i+1]+nums2[j], i+1, j]);
            if j+1 < len(nums2) and [i, j+1] not in visited:
                heapq.heappush(h, [nums1[i]+nums2[j+1], i, j+1]);
            kCounter += 1;
        return result;

sol = Solution();
print(sol.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 20));