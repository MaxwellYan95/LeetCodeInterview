class Node:
    def __init__(self, key: int, value: int):
        self.key = key;
        self.value = value;
        self.next = None;
        self.prev = None;

class LRUCache:

    def __init__(self, capacity: int):
        self.front = None;
        self.end = None;
        self.capacity = capacity;
        self.length = 0;


    def put(self, key: int, value: int) -> None:
        getVal = self.get(key);
        if getVal != -1:
            self.front.value = value;
        else:
            self.add(key, value);
            if self.length > self.capacity:
                self.delete(self.back);


    def get(self, key: int) -> int:
        traverse = self.front;
        for i in range(self.length):
            if traverse.key == key:
                result = traverse.value;
                self.add(key, result);
                self.delete(traverse);
                return result;
            traverse = traverse.next;
        return -1;

    def delete(self, location: Node):
        oldKey = location.key;
        previous = location.prev;
        nextOne = location.next;
        previous.next = location.next;
        nextOne.prev = location.prev;
        self.length -= 1;
        if oldKey == self.back.key:
            self.end = self.end.prev;
        if oldKey == self.front.key:
            self.front = self.front.next;

    def add(self, key: int, value: int):
        if self.front == None:
            self.front = Node(key, value);
            self.back = self.front;
            self.front.next = self.back;
            self.front.prev = self.back;
        else:
            oldFront = self.front;
            self.front = Node(key, value);
            oldFront.prev = self.front;
            self.front.next = oldFront;
            self.back.next = self.front;
            self.front.prev = self.back;
        self.length += 1;




sol = LRUCache(2);
sol.put(1, 1);
sol.put(2, 2);
print(sol.get(1));
sol.put(3, 3);
print(sol.get(2));
sol.put(4, 4);
print(sol.get(1));
print(sol.get(3));
print(sol.get(4));