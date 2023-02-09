from LinkedList import LinkedList as LL
import unittest

class TestLL(unittest.TestCase):

    def test_addfirst_remfirst(self):
        n = 8
        ll = LL()

        for i in range(n):
            self.assertEqual(len(ll), i)
            ll.add_first(i)

        #head->7-6-5-4-3-2-1-0->None
        #Tail----------------^

        for i in range(n):
            self.assertEqual(len(ll), n-i)
            self.assertEqual(ll.remove_first(), n-1-i)

unittest.main()
