class MedianFinder:

    def __init__(self):
        self.numbers = [];

    def addNum(self, num: int) -> None:
        if len(self.numbers) == 0:
            self.numbers.append(num);
            return;
        size = len(self.numbers);
        mid = int(size/2);
        while True:
            if mid == len(self.numbers)-1:
                if self.numbers[mid] < num:
                    self.numbers = self.numbers + [num];
                else:
                    self.numbers = self.numbers[1:(size-1)] + [num] + self.numbers[size-1:];
                break;
            elif mid == 0:
                if num < self.numbers[mid]:
                    self.numbers = [num] + self.numbers;
                else:
                    self.numbers = self.numbers[0] + [num] + self.numbers[1:];
                break;
            elif self.numbers[mid-1] < num < self.numbers[mid]:
                self.numbers = self.numbers[:mid] + [num] + self.numbers[mid:];
                break;
            elif self.numbers[mid-1] > num:
                mid = int(mid/2);
            elif num > self.numbers[mid]:
                mid += int(mid/2);

    def findMedian(self) -> float:
        mid = int(len(self.numbers)/2);
        if len(self.numbers) % 2 == 0:
            return float(self.numbers[mid] + self.numbers[mid-1]) / 2;
        else:
            return self.numbers[mid];

median = MedianFinder();
median.addNum(1);
median.addNum(2);
print(median.findMedian());
median.addNum(3);