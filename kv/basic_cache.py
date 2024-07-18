import time as time_time


class LRUCache:
    def __init__(self, size):
        """Initialize the LRUCache with max size."""
        self.size = size
        self.cache = {}
        self.access = {}
        self.time = 0

    def get(self, key):
        """get item from cache. return None if item is not present or expired"""
        self.time += 1
        if key in self.cache and self.cache[key][1] > time_time.time():
            self.access[key] = self.time
            return self.cache[key][0]
        return None

    def set(self, key, value, duration):
        """set value at key with expiration duration (time in seconds)"""
        self.time += 1
        if len(self.cache) >= self.size:
            # evict least recently used item in the cache
            old_key = min(self.access, key=lambda x: self.access[x])
            self.cache.pop(old_key)
            self.access.pop(old_key)
        expire_time = time_time.time() + duration
        self.cache[key] = (value, expire_time)
        self.access[key] = self.time

    def delete(self, key):
        """remove item from cache if it exists"""
        if key in self.cache:
            del self.access[key]
            self.cache.pop(key)


cache = LRUCache(3)  # size 3

cache.set('a', 1, 2)  # expires in 2 secs
cache.set('b', 3, 4)  # expires in 4 secs
cache.set('c', 5, 6)

print(cache.get('a'))
print(cache.get('d'))

cache.set('e', 7, 8)
cache.set('f', 9, 10)
print(cache.get('f'))  # should return None since its evicted due to size limit
