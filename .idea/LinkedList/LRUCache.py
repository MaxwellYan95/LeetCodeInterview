class Node:
    def __init__(self, key: int, value: int):
        self.key = key;
        self.value = value;
        self.next = None;



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = None;
        self.capacity = capacity;


    def get(self, key: int) -> int:
        if self.cache == None:
            return -1;
        if (self.cache.key == key):
            return self.cache.value;
        def traverse(prev: Node, cur: Node):
            return traverse(cur, cur.next);
            if cur.key == key:
                res = cur.value;
                prev.next = cur.next;
                return res;
            if cur.next == None:
                return -1;
        result = traverse(self.cache, self.cache.next);
        if result != -1:
            first = self.cache;
            self.cache = LRUCache()


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
                if traverse.key == key:
                    traverse.value = value;
                    return;
            traverse.next = Node(key, value);
            if counter == self.capacity:
                self.cache = first.next;

sol = LRUCache(3);
sol.put(1, 1);
sol.put(2, 2);
sol.put(3, 3);
sol.put(4, 4);
sol.put(3, 4);
sol.put(5, 5);
