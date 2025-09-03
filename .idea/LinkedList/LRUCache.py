class Node:
    def __init__(self, key: int, value: int):
        self.key = key;
        self.value = value;
        self.next = None;
    def setKey(self, key: int):
        self.key = key;
    def setValue(self, value: int):
        self.value = value;



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = None;
        self.capacity = capacity;
        self.length = 0;


    def get(self, key: int) -> int:
        if self.cache == None:
            return -1;
        if (self.cache.key == key):
            return self.cache.value;
        def traverse(prev: Node, cur: Node):
            if cur == None:
                return -1;
            if cur.key == key:
                oldKey = cur.key;
                res = cur.value;
                prev.next = cur.next;
                oldCache = self.cache;
                self.cache = Node(oldKey, res);
                self.cache.next = oldCache;
                return res;
            if cur.next == None:
                return -1;
            return traverse(cur, cur.next);
        result = traverse(self.cache, self.cache.next);
        return result;

    # removes last element
    def removeLast(self):
        if self.cache.next == None:
            self.cache = None;
        else:
            traverse = self.cache;
            for i in range(self.capacity-2):
                traverse = traverse.next;
            traverse.next = None;

    def put(self, key: int, value: int) -> None:
        if self.cache == None:
            self.cache = Node(key, value);
            self.length += 1;
            return;
        if self.get(key):
            self.cache.value = value;
            return;
        if self.length == self.capacity:
            self.removeLast();
        else:
            self.length += 1;
        first = self.cache;
        self.cache = Node(key, value);
        self.cache.next = first;

sol = LRUCache(2);
sol.put(2, 1);
sol.put(1, 1);
sol.put(2, 3);
sol.put(4, 1);
print(sol.get(1));
print(sol.get(2));
