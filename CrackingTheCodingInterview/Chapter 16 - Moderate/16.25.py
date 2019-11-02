class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.usage_frequency = []
        self.lru = {}

    def get(self, key):
        if key in self.lru:
            self.usage_frequency.remove(key)
            self.usage_frequency.append(key) # move to the back
            return self.lru[key]
        return -1

    def put(self, key, value):
        if key in self.lru:
            self.lru[key] = value
            self.usage_frequency.remove(key)
            self.usage_frequency.append(key) # move to the back
            return None

        if len(self.usage_frequency) == self.capacity:
            del self.lru[self.usage_frequency[0]]
            del self.usage_frequency[0]

        self.usage_frequency.append(key)
        self.lru[key] = value
        
if __name__ == "__main__":
	main()