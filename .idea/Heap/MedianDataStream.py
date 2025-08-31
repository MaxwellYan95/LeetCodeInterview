

import heapq;

class MedianFinder:

    def __init__(self):
        self.smallest = [];
        self.largest = [];
        heapq.heapify(self.smallest);
        heapq.heapify(self.largest);

    def addNum(self, num: int) -> None:
        if len(self.smallest) == len(self.largest):
            heapq.heappush(self.largest, -heapq.heappushpop(self.smallest, num));
        else:
            heapq.heappush(self.smallest, -heapq.heappushpop(self.largest, -num))

    def findMedian(self) -> float:
        if len(self.smallest) == len(self.largest):
            m1 = heapq.heappop(self.largest);
            heapq.heappush(self.largest, m1);
            m2 = heapq.heappop(self.smallest);
            heapq.heappush(self.smallest, m2);
            return float(m2 - m1) / 2;
        else:
            m = heapq.heappop(self.largest);
            heapq.heappush(self.largest, m);
            return -m;

median = MedianFinder();
median.addNum(1);
median.addNum(2);
print(median.findMedian());
median.addNum(3);
median.addNum(4);
print(median.findMedian());