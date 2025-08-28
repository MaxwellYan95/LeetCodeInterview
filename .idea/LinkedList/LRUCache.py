class Node:
    def __init__(self, key: int, value: int):
        self.key = key;
        self.value = value;
        self.next = None;



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = None;
        self.capacity = capacity;


    # def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:
        if self.cache == None:
            self.cache = Node(key, value);
        else:
            counter = 1;
            traverse = self.cache;
            first = self.cache;
            while traverse.next != None and counter != self.capacity:
                traverse = traverse.next;
                counter += 1;
            traverse.next = Node(key, value);
            if counter == self.capacity:
                self.cache = first.next;

sol = LRUCache(3);
sol.put(1, 1);
sol.put(2, 2);
sol.put(3, 3);
sol.put(4, 4);
sol.put(5, 5);
