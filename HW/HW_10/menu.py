from waitlist import Waitlist
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:
            
            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                #TODO """Add a customer to the waitlist"""

                # get customer name
                name = input("Enter the customer's name: ")

                # get customer time in HH:MM format - then validate that it is in correct format
                time = input("Enter the customer's reservation time (HH:MM): ")

                # add customer to the waitlist
                result = self.waitlist.add_customer(name, time)

                # while loop to ensure that time is a valid format
                while result == False:
                    time = input('Enter valid time: ')
                    result = self.waitlist.add_customer(name, time)

                # print
                print(f"\n{name} has been added to the waitlist at {time}\n")


            elif choice == "2":
                #TODO"""Seat the next customer"""

                # get the next customer in the waitlist
                customer, time = self.waitlist.seat_customer()

                # print
                print(f'\nSeated customer: {customer}, reservation time: {time}\n')


            elif choice == "3":
                #TODO"""Change the time of a customer's reservation"""
                
                # get customer name - if name is not in heap - returns false
                name = input("Enter the customer's name: ")

                # get customer time in HH:MM format - then validate that it is in correct format
                new_time = input("Enter the new time of the reservation (HH:MM): ")

                # ensure that time is in a valid format using while loop
                while self.waitlist.validate_time(new_time) == False:
                    new_time = input('Enter a valid new time: ')
                result = self.waitlist.change_reservation(name, new_time)
                if result is False:
                    print('Customer not in waitlist')

                # print
                else:

                    print(f"\n{name}'s reservation time has been changed to {time}\n\n")


            elif choice == "4":
                #TODO"""Peek at the next customer"""
                
                # get the next customer in the waitlist
                customer = self.waitlist.peek()

                # if returned item is None - don't end program
                if customer == None:
                    print("The waitlist is empty. No customers to seat.")
                    continue
                # print
                else: print(f'\nThe next customer on the waitlist is: {customer[0]}, reservation time: {customer[1]}\n')


            elif choice == "5":
                #TODO"""Print the waitlist"""
            
                print('---------------------------------------------------')
                
                # returned value from print_reservation_list is assigned to reservation_list var
                reservation_list = self.waitlist.print_reservation_list()

                # checks to see that waitlist is not empty
                if reservation_list != []:
                    # prints out name and time from reservation_list 
                    for name, time in reservation_list:
                        print(f'The next customer on the waitlist is: {name}, reservation time: {time}')
                else:
                    print("The waitlist is empty. No customers to seat.")

                print('\n\n---------------------------------------------------')


            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")
    

s = Menu()
s.run()

