import functools
import inspect
import logging
 
logging.basicConfig(level = logging.INFO)

class Gen:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.curr = 0

    def __next__(self):
        if self.curr < self.n:
            res = self.a ** self.curr
            self.curr += 1
            return res
        else:
            raise StopIteration

    def __iter__(self):
        return self

generator = Gen(2, 5)
for power in generator:
    logging.info(f" {power}")