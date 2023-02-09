from Stack import Stack, Queue
import unittest

class TestStack(unittest.TestCase):
    'some tests for a stack class'

    def test_pushpop(self):
        n = 4

        s = Stack()

        for i in range(n):
            s.push(i)

        for i in range(n):
            self.assertEqual(s.pop(), n-1-i)

class TestQueue(unittest.TestCase):
    ' some tests for a stack class'
    
    def test_enqdeq(self):
        n = 4

        q = Queue()

        for i in range(n):
            q.enqueue(i)

        for i in range(n):
            self.assertEqual(q.dequeue(), i)

unittest.main()