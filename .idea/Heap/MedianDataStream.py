

import heapq;

class MedianFinder:

    def __init__(self):
        self.numbers = [];
        heapq.heapify(self.numbers);

    def addNum(self, num: int) -> None:
        heapq.heappush(self.numbers, num);

    def findMedian(self) -> float:
        mid = int(len(self.numbers)/2);
        temp = heapq.nsmallest(mid+1, self.numbers);
        if len(self.numbers) % 2 == 0:
            return float(temp[mid-1] + temp[mid]) / 2;
        else:
            return temp[mid];

median = MedianFinder();
median.addNum(1);
median.addNum(2);
print(median.findMedian());
median.addNum(3);
median.addNum(4);
print(median.findMedian());