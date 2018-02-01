from heapq import heappush, heappop, heapify
from time  import time

class Heap(object):
    def __init__(self, items = [], key = lambda item: item):
        self.key = key
        self.items = [(key(item), time(), item) for item in items]

        heapify(self.items)

    ##################################################################
    # Heap Operations
    ##################################################################

    def insert(self, item):
        heappush(self.items, (self.key(item), time(), item))

    def delete(self):
        return heappop(self.items)[2]

    def isEmpty(self):
        return not self.items

    ##################################################################
    # Method Overrides
    ##################################################################

    def __len__(self):
        return len(self.items)
