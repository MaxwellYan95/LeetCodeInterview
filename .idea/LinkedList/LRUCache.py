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

    #def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:
        if self.front == None:
            self.front = Node(key, value);
            self.back = Node(key, value);
            self.front.next = self.back;
            self.front.prev = self.back;
            self.back.next = self.front;
            self.back.prev = self.front;
        else:
            oldFront = self.front;
            self.front = Node(key, value);
            self.front.next = oldFront;
            self.front.prev = self.back;

sol = LRUCache(2);
sol.put(2, 1);
sol.put(3, 2);

