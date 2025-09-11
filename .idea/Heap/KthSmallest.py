import heapq;
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        minH = [];
        results = [];
        heapq.heapify(minH);
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(minH, [n1+n2, (n1, n2)]);
        for _ in range(k):
            results.append(heapq.heappop(minH)[1]);
        return results;

sol = Solution();
print(sol.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 20));