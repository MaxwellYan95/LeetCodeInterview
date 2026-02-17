class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.lst = sorted(nums);
        self.k = k

    def add(self, val: int) -> int:
        if len(self.lst) == 0:
            self.lst.append(val)
        elif val <= self.lst[0]:
            self.lst = [val] + self.lst
        elif val >= self.lst[len(self.lst)-1]:
            self.lst.append(val)
        else:
            for index in range(1, len(self.lst)):
                if val <= self.lst[index]:
                    self.lst = self.lst[:index] + [val] + self.lst[index:]
                    break;
        kth = len(self.lst) - self.k
        return self.lst[kth];


obj = KthLargest(3, [4,5,8,2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)