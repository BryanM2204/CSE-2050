from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        'Tests if item is in dll using the contains method'
        dll = DLL(range(10)) #add 0-9 to dll

        #test if items are in dll
        self.assertEqual(0 in dll, True)
        self.assertEqual(5 in dll, True)
        self.assertEqual(19 in dll, False)    

    def test_neighbors(self):
        'Tests if item is in dll using the neighbors method'
        dll = DLL(range(10)) #add 0-9 to dll

        #test that neighbors returns the correct items
        self.assertEqual(dll.neighbors(5), (4,6))
        self.assertEqual(dll.neighbors(1), (0,2))
        self.assertEqual(dll.neighbors(0), (None,1)) #edge case - testing neighboring nodes for head
        self.assertEqual(dll.neighbors(9), (8,None)) #edge case - testing neighboring nodes for tail

    def test_remove_item(self):
        'Tests if item is removed from dll using the remove_item method'
        dll = DLL(range(10)) #add 0-9 to dll

        #tests that remove_items correctly removes the item from DLL
        self.assertEqual(dll.remove_node(0), 0)         #edge case - testing removal of head 
        self.assertEqual(dll.neighbors(1), (None, 2))   #test to see if neighboring nodes were correctly stitched together
        self.assertEqual(len(dll), 9)                   #test to see if length was correctly updated

        self.assertEqual(dll.remove_node(9), 9)         #edge case - testing removal of tail
        self.assertEqual(dll.neighbors(8), (7, None))   #test to see if neighboring nodes were correctly stitched together
        self.assertEqual(len(dll), 8)                   #test to see if length was correctly updated

        self.assertEqual(dll.remove_node(5), 5)         #test on node in the middle of dll
        self.assertEqual(dll.neighbors(4), (3, 6))      #test to see if neighboring nodes were correctly stitched together
        self.assertEqual(len(dll), 7)                   #test to see if length was correctly udpated

unittest.main()
