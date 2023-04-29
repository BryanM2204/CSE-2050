import unittest
from waitlist import Waitlist, Time

class TestWaitlist(unittest.TestCase):
    """Tests the Waitlist Class"""
    def setUp(self):
        """Sets up waitlist and adds customers to it that will be used throughout the tests"""
        self.waitlist = Waitlist()
        
        #add_customer is called upon to add 4 customers
        self.waitlist.add_customer("Bryan", "02:00")
        self.waitlist.add_customer("Jazz", "12:30")
        self.waitlist.add_customer("Peter", "04:30")
        self.waitlist.add_customer("Justin", "18:00")


    def test_add_customer(self):
        """Tests the add_customer method"""
        # adds a new customer that has the highest time priority
        self.waitlist.add_customer("John", "01:00")
        # use peek() to ensure that customer was properly added to waitlist in correct position
        self.assertEqual(self.waitlist.peek(), ("John", Time(1, 0)))        


    def test_peek(self):
        """Tests the peek method"""

        # use peek() to ensure that customer was properly added to waitlist in correct position
        self.assertEqual(self.waitlist.peek(), ("Bryan", Time(2, 0)))
        # seat_customer is used to change the waitlist - remove customer and check if peek keeps time priority into account
        self.waitlist.seat_customer()

        self.assertEqual(self.waitlist.peek(), ("Peter", Time(4, 30)))
        self.waitlist.seat_customer()

        self.assertEqual(self.waitlist.peek(), ("Jazz", Time(12, 30)))
        self.waitlist.seat_customer()

        self.assertEqual(self.waitlist.peek(), ("Justin", Time(18, 0)))
        
    
    def test_seat_customer(self):
        """Tests the seat_customer method"""

        # tests that the seat_customer is equal to the expected customer's name and time
        self.assertEqual(self.waitlist.seat_customer(), ("Bryan", Time(2, 0)))
        # peek() is used in order to make sure which costumer is next for seat_customer()
        self.assertEqual(self.waitlist.peek(), ("Peter", Time(4, 30)))
        self.assertEqual(self.waitlist.seat_customer(), ("Peter", Time(4, 30)))

        self.assertEqual(self.waitlist.peek(), ("Jazz", Time(12, 30)))
        self.assertEqual(self.waitlist.seat_customer(), ("Jazz", Time(12, 30)))

        self.assertEqual(self.waitlist.peek(), ("Justin", Time(18, 0)))
        self.assertEqual(self.waitlist.seat_customer(), ("Justin", Time(18, 0)))

        # after all customers were seated - the length of the list should be 0
        self.assertEqual(len(self.waitlist), 0)


    def test_print_reservation_list(self):
        """Tests that """
        # print_reservation_list returns a list containing tuples of customer names and times
        reservation_list = self.waitlist.print_reservation_list()

        copy_list = []
        for name, time in reservation_list:
            # name and times appended to copy_list
            copy_list.append(f'The next customer on the waitlist is: {name}, time: {time}')
        # ensure that copy_list is the same to the expected string
        self.assertEqual(copy_list, ['The next customer on the waitlist is: Bryan, time: 02:00', 'The next customer on the waitlist is: Peter, time: 04:30', 'The next customer on the waitlist is: Jazz, time: 12:30', 'The next customer on the waitlist is: Justin, time: 18:00'])        


    def test_change_reservation(self):
        """Tests the change_reservation method"""
        # as the customers were initialized in setUp - change_reservation is used to change it
        self.waitlist.change_reservation("Bryan", "01:00")
        # peek() is used in this insatnce to ensure that time was properly changed - and with it time priority
        self.assertEqual(self.waitlist.peek(), ("Bryan", Time(1, 0)))

        self.waitlist.change_reservation("Jazz", "13:30")
        
        # seat_customer is used to remove first customer with highets time priority - in this instance it is Bryan
        self.waitlist.seat_customer()

        # peek() used to check which is next customer in line
        self.assertEqual(self.waitlist.peek(), ("Peter", Time(4, 30)))
        self.waitlist.change_reservation("Peter", "03:30")

        # checks to see that time was changed
        self.assertEqual(self.waitlist.peek(), ("Peter", Time(3, 30)))
        self.waitlist.seat_customer()

        # check to see that time was properly changed from line 77
        self.assertEqual(self.waitlist.peek(), ("Jazz", Time(13, 30)))
        self.waitlist.seat_customer()

        # final customer with lowest priority remains
        self.assertEqual(self.waitlist.peek(), ("Justin", Time(18, 0)))

    
unittest.main()