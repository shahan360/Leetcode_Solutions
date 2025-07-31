class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = [] # To keep track of the order of keys for LRU
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end of the order list
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the key to the end of the order list
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if self.size >= self.capacity:
                # Remove the least recently used item
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
                self.size -= 1
            # Add the new key-value pair
            self.cache[key] = value
            self.order.append(key)
            self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)