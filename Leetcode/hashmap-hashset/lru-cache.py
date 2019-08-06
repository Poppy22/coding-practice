class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.usage_frequency = []
        self.lru = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru:
            self.usage_frequency.remove(key)
            self.usage_frequency.append(key)
            return self.lru[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.lru:
            self.lru[key] = value
            self.usage_frequency.remove(key)
            self.usage_frequency.append(key)
            return None
        
        if len(self.usage_frequency) == self.capacity:
            del self.lru[self.usage_frequency[0]]
            del self.usage_frequency[0]
            
        self.usage_frequency.append(key)
        self.lru[key] = value
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)