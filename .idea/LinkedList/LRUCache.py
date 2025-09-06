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
        if self.length != self.capacity:
            self.add(key, value);
        else:
            contained = self.get(key);
            if (contained == -1):
                self.delete(self.back);
                self.back = self.back.prev;
                self.add(key, value);
            else:
                self.delete(self.front);
                self.front = self.front.next;
                self.add(key, contained);

    def get(self, key: int) -> int:
        for i in range(self.length):
            if (self.front.key == self.back.key):
                self.back = self.back.prev;
            if self.front.key == key:
                return self.front.value;
            else:
                self.front = self.front.next;
        return -1;

    def delete(self, location: Node):
        if self.length == 1:
            self.front = None;
            self.back = None;
        else:
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