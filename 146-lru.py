from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.cache = dict()

    def get(self, key: int) -> int:
        if key in self.queue:
            self.queue.remove(key)
            self.queue.insert(0, key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.queue:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.insert(0, key)
            return
        if len(self.cache) >= self.capacity:
            t = self.queue.pop()
            self.queue.insert(0, key)
            del self.cache[t]
            self.cache[key] = value
        else:
            self.queue.insert(0, key)
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)