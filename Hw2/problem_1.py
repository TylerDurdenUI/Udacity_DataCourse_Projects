class LRU_Cache(object):
    def __init__(self,capacity):
        self.cap = capacity
        self.vals = {} 
        self.key_order = []
    def get(self,key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        return self.vals.get(key,-1)
    def set(self,key,value):
        # Set the value if the key is not present in the cache. 
        # If the cache is at capacity remove the oldest item.
        self.vals[key] =value
        self.key_order.append(key)
        if len(self.key_order) > self.cap:
            pop_key = self.key_order.pop(0) # Remove oldest key from list
            self.vals.pop(pop_key) # Remove the value with the oldest key in the dictionary

# testing case
if __name__=='__main__':
    our_cache = LRU_Cache(3)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)


    print(our_cache.get(1) )      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    # Empty LRU_Cache object test case
    our_cache = LRU_Cache(0)
    our_cache.set(1, 1)
    print(our_cache.get(1) )      # returns -1 since capacity is 0
    print(our_cache.get(2) )      # returns -1 since capacity is 0

