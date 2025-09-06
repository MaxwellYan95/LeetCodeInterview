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
        if self.front == None:
            self.front = Node(key, value);
            self.back = self.front;
            self.front.next = self.back;
            self.front.prev = self.back;
            self.length += 1;
        elif self.length != self.capacity:
            oldFront = self.front;
            self.front = Node(key, value);
            oldFront.prev = self.front;
            self.front.next = oldFront;
            self.back.next = self.front;
            self.front.prev = self.back;
            self.length += 1;
        else:
            contained = self.get(key);
            if contained != -1:
                self.front.value = value;
            else:
                self.front = self.front.prev;
                self.back = self.back.prev;
                self.front.key = key;
                self.front.value = value;

    def get(self, key: int) -> int:
        for i in range(self.capacity):
            if self.front.key == key:
                return self.front.value;
            else:
                self.front = self.front.next;
                self.back = self.back.next;
        return -1;




sol = LRUCache(2);
sol.put(2, 1);
sol.put(3, 2);
sol.put(5, 4);
print();
