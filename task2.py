# task2.py
from collections import deque

class FIFOBufferList:
    def __init__(self, size):
        self.size = size
        self.buffer = []

    def add(self, item):
        if len(self.buffer) == self.size:
            self.buffer.pop(0)  
        self.buffer.append(item)

    def get(self):
        if self.buffer:
            return self.buffer.pop(0)
        return None


class FIFOBufferDeque:
    def __init__(self, size):
        self.size = size
        self.buffer = deque()

    def add(self, item):
        if len(self.buffer) == self.size:
            self.buffer.popleft() 
        self.buffer.append(item)

    def get(self):
        if self.buffer:
            return self.buffer.popleft()
        return None


if __name__ == "__main__":
    print("FIFO с использованием списка:")
    fifo_list = FIFOBufferList(3)
    fifo_list.add(1)
    fifo_list.add(2)
    fifo_list.add(3)
    fifo_list.add(4)
    print(fifo_list.buffer) 
    print(fifo_list.get())  

    print("\nFIFO с использованием deque:")
    fifo_deque = FIFOBufferDeque(3)
    fifo_deque.add(1)
    fifo_deque.add(2)
    fifo_deque.add(3)
    fifo_deque.add(4)
    print(fifo_deque.buffer)  
    print(fifo_deque.get()) 
