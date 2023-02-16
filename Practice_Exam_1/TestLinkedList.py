from LinkedList import LinkedList as LL
import unittest

class TestLinkedList(unittest.TestCase):
    def test_addlast_removelast(self):
        n = 10
        ll = LL()

        for i in range(n):
            self.assertEqual(len(ll), i)
            ll.add_last(i)

        for i in range(n):
            self.assertEqual(len(ll), n-i)
            self.assertEqual(ll.remove_last(n), n-1-i)

unittest.main()