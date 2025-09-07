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
            return;
        self.add(key, value);
        if self.length > self.capacity:
            self.delete(self.back);
            self.back = self.back.prev;


    def get(self, key: int) -> int:
        traverse = self.front;
        result = -1;
        for i in range(self.length):
            if traverse.key == key:
                result = traverse.value;
                break;
            traverse = traverse.next;
        if result != -1:
            self.add(key, result);
            self.delete(traverse);
        return result;

    def delete(self, location: Node):
        location.prev.next = location.next;
        location.next.prev = location.prev;
        self.length -= 1;

    def add(self, key: int, value: int):
        if self.front == None:
            self.front = Node(key, value);
            self.back = self.front;
            self.front.next = self.back;
            self.front.prev = self.back;
            self.length += 1;
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