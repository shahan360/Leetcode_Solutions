class MyHashMap:

    def __init__(self):
        # Initialize the HashMap with a fixed size
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def hashfunction(self, key):
        # Hash function to compute the index for a given key
        return key % self.size 

    def put(self, key: int, value: int) -> None:
        index = self.hashfunction(key)
        # Check if the key already exists in the map
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                # Update the value if the key exists
                self.map[index][i] = (key, value)
                return
        # If the key does not exist, append a new key-value pair
        self.map[index].append((key, value))
        return

    def get(self, key: int) -> int:
        index = self.hashfunction(key)
        # Search for the key in the corresponding bucket
        for k, v in self.map[index]:
            if k == key:
                return v
        # Return -1 if the key does not exist
        return -1

    def remove(self, key: int) -> None:
        index = self.hashfunction(key)
        # Search for the key in the corresponding bucket
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                # Remove the key-value pair if found
                del self.map[index][i]
                return
        # If the key does not exist, do nothing
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)