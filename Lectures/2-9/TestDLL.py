from DLL import DoublyLinkedList as DLL
import unittest

class TestDLL(unittest.TestCase):
    'test cases for doubly-linked list'

    def test_addfirstremovelast(self):
        'add and remove from beginning of dll'
        n = 8
        dll = DLL()

        #add n items
        for i in range(n):
            self.assertEqual(len(dll), i)
            dll.add_first(i)

        #remove n items
        for i in range(n):
            self.assertEqual(len(dll), n-i)
            self.assertEqual(dll.remove_last(i), i)

unittest.main()