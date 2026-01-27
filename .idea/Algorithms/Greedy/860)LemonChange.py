import heapq

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stack = []
        heapq.heapify(stack);
        for payment in bills:
            curAmount = payment;
            heapq.heappush(stack, curAmount)
            while curAmount > 5:
                curAmount -= heapq.heappop(stack);
                heapq.heapify(stack);
            if curAmount < 5:
                return False;
        return True;

sol = Solution()
print(sol.lemonadeChange([5,5,5,10,20]))



