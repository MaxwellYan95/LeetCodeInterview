class SmallestInfiniteSet:


    def __init__(self):
        self.set = set([num for num in range(1, 1001)]);

    def popSmallest(self) -> int:
        minimum = min(self.set);
        self.set.remove(minimum);
        return minimum


    def addBack(self, num: int) -> None:
        self.set.add(num)