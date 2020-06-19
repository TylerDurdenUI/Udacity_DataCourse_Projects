import hashlib
from datetime import datetime as dt
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
        self.next = None # add next attribute to link two blocks
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self,value=None):
        if value==None:
            return
        node = self.head
        self.size += 1
        if not node: # empty Blockchain
            self.head= Block(dt.now(),value,None) # Initiate first block
        else:
            while node.next: # move the pointer node to the end, till next is None
                node = node.next
            node.next = Block(dt.now(),value,node.hash)

# testing case

chain = Blockchain()
chain.append('data for a')
chain.append(2020)
chain.append('data for c')
chain.append(None)

# head block:
node = chain.head
print("============\nBlock timestamp: {};\nBlock data: {};\nBlock SHA256 HASH: {};\nPrevious HASH: {}.\n============".format(node.timestamp,node.data,node.hash,node.previous_hash))
b = chain.head.next
node = b 
print("============\nBlock timestamp: {};\nBlock data: {};\nBlock SHA256 HASH: {};\nPrevious HASH: {}.\n============".format(node.timestamp,node.data,node.hash,node.previous_hash))
c = chain.head.next.next
node = c
print("============\nBlock timestamp: {};\nBlock data: {};\nBlock SHA256 HASH: {};\nPrevious HASH: {}.\n============".format(node.timestamp,node.data,node.hash,node.previous_hash))

print(b.hash == c.previous_hash)
# True


blockchain = Blockchain()
blockchain.append() # empty input
blockchain.append("Non empty input")
node = blockchain.head
print("============\nBlock timestamp: {};\nBlock data: {};\nBlock SHA256 HASH: {};\nPrevious HASH: {}.\n============".format(node.timestamp,node.data,node.hash,node.previous_hash))

