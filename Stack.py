from inspect import stack
import numpy as np

class Stack:
    def __init__(self, arrsize=10):
        self.arrmax = arrsize
        self.contents = np.empty(self.arrmax, np.str0)
        self.head = -1
        self.count = 0
        self.full = False

    def add(self, elein):
        if not self.full:
            if (self.head + 1 == self.arrmax):
                self.head = 0
            else:
                self.head += 1
            self.contents[self.head]=elein
            self.count +=1
        else:
            raise Exception("The stack is full")
    
    def pop(self):
        while self.count > 0:
            out = self.contents[self.head]
            self.contents[self.head] = ''
            if (self.head - 1 < 0):
                self.head = self.arrmax -1
            else:
                self.head -= 1
            self.count -=1
            return out

    def isempty(self):
        return self.count == 0

    def __repr__(self):
        return str(self.contents)

    def __iter__(self):
        return StackIter(self, self.head)

    def __len__(self):
        return self.count
 
class StackIter():
    def __init__(self, stack, head):
        self.stk = stack
        self.head = head

    def __next__(self):
        if self.stk.isempty():
            raise StopIteration
        else:
            return self.stk.pop()

    

if __name__ == '__main__':
    s = Stack()
    for i in range(1, s.arrmax):
        s.add(str(i))
        print(str(i))
    print(s)
    print(s.pop())
    print(s)
    s.add('a')
    s.add('b')
    print(s)
    print(s.pop())
    print(s.pop())
    print(s)
    t = Stack()
    t.add('t')
    print(t)
    print(len(s))
    for i in s:
        print(i)
    print(s)

