import unittest
from blockchain import Blockchain, Block, Transaction, Ledger

class TestTransaction(unittest.TestCase):
    """Tests Transaction"""

    def test_transaction(self):
        """Sets up users and the transaction amount"""
        t = Transaction('user1', 'user2', 50)
        # test to see that transaction works in initializing correctly and printing out the correct statement
        self.assertEqual(str(t), "Transaction(from_user=user1, to_user=user2, amount=50)")

class TestBlock(unittest.TestCase):
    """Tests functionallity of Block"""

    def setUp(self):
        """Sets up the block"""
        # 2 transactions set up
        self.t1 = Transaction('user1', 'user2', 50)
        self.t2 = Transaction('user2', 'user3', 20)
        # Block created with previous hash provided
        self.block = Block([self.t1, self.t2], previous_hash='123')

    def test_add_transaction(self):
        """Tests to see if the transaction is added to the block"""
        # adds a transaction to the block
        t3 = Transaction('user3', 'user1', 10)
        self.block.add_transaction(t3)
        # tests to see if transaction is equal to the expected output
        self.assertEqual(self.block.transactions, [self.t1, self.t2, t3])
        self.assertIn(t3, self.block.transactions)

class TestLedger(unittest.TestCase):
    """Tests functionality of Ledger"""

    def setUp(self):
        """Initializes ledger class"""
        self.ledger = Ledger()
        self.user1 = 'user1'
        self.user2 = 'user2'

    def test_deposit(self):
        """Tests to see if the deposit function works"""
        # deposits 50 coins into user1's account
        self.ledger.deposit('user1', 50)
        # tests to see that amount is updated correctly
        self.assertEqual(self.ledger._hashmap['user1'], 50)

    def test_transfer(self):
        """Tests to see if the transfer function works"""
        # deposits 50 coins into user1's account
        self.ledger.deposit('user1', 50)
        # transfers 20 coins from user1 to user2
        self.assertTrue(self.ledger.transfer('user1', 'user2', 20))
        # tests to see that amount is updated correctly
        self.assertEqual(self.ledger._hashmap['user1'], 30)

    def test_has_funds(self):
        """Tests to see if the has_funds function works"""
        # Checks to see that test returns false
        self.assertFalse(self.ledger.has_funds('user1', 50))
        # Deposits 50 coins into user1's account
        self.ledger.deposit('user1', 50)
        # Checks to see that test returns true
        self.assertTrue(self.ledger.has_funds('user1', 50))
        # Checks to see that test returns false
        self.assertFalse(self.ledger.has_funds('user1', 150))

class TestBlockchain(unittest.TestCase):
    """Tests functionality of Blockchain"""

    def setUp(self):
        """Sets up Blockchain"""
        self.bc = Blockchain()
        self.user1 = 'Alice'
        self.user2 = 'Bob'

    def test_create_genesis_block(self):
        """Tests genesis_block"""
        # genesis block already created when Blockchain is initialized to self.bc
        self.assertEqual(len(self.bc._blockchain), 1)
        self.assertEqual(len(self.bc._blockchain[0].transactions), 1)
        # tests to see that user is 'Root' and the amounts match with the default amounts
        self.assertEqual(self.bc._blockchain[0].transactions[0].from_user, 'ROOT')
        self.assertEqual(self.bc._blockchain[0].transactions[0].to_user, 'ROOT')
        self.assertEqual(self.bc._blockchain[0].transactions[0].amount, 999999)
        self.assertEqual(self.bc._bc_ledger._hashmap['ROOT'], 999999)

    def test_distribute_mining_reward(self):
        """Tests the distribute mining reward method"""
        # distributes mining reward to user1
        self.bc.distribute_mining_reward(self.user1)
        # tests to see that the block is added and the transaction is correct
        self.assertEqual(len(self.bc._blockchain), 2)
        self.assertEqual(len(self.bc._blockchain[1].transactions), 1)
        # tests to see that the user is "Root", the reciever is the self.user1,, and the amount is correct
        self.assertEqual(self.bc._blockchain[1].transactions[0].from_user, 'ROOT')
        self.assertEqual(self.bc._blockchain[1].transactions[0].to_user, self.user1)
        self.assertEqual(self.bc._blockchain[1].transactions[0].amount, 1000)
        self.assertEqual(self.bc._bc_ledger._hashmap[self.user1], 1000)

    def test_add_block(self):
        """Tests the add_block method"""
        # creates a Block with a transaction btw. user1 and user2 of amount 500
        block = Block([Transaction(self.user1, self.user2, 500)])
        # adds the block to the blockchain
        self.bc.add_block(block)
        # Checks length of the blockchain - with it being 2 due to the genesis block
        self.assertEqual(len(self.bc._blockchain), 2)
        self.assertEqual(len(self.bc._blockchain[1].transactions), 1)
        self.assertEqual(self.bc._blockchain[1].transactions[0].from_user, self.user1)
        self.assertEqual(self.bc._blockchain[1].transactions[0].to_user, self.user2)
        self.assertEqual(self.bc._blockchain[1].transactions[0].amount, 500)

    # TEST for insufficient funds when transferring - use the ledger class when checking
    def test_insufficient_funds(self):
        """tests case where the user has insufficient funds in their account to perform a transaction"""
        ledger = Ledger()
        self.bc.distribute_mining_reward(self.user1)
        # Assuming that user1 has 10000 in their account
        if ledger.has_funds(self.user1, 500):
            self.assertTrue(self.bc.add_block(Block([Transaction(self.user1, self.user2, 5000)])))

    def test_valid_chain(self):
        """tests case where a block is tampered with - the block that is tampered with should be in a returned list"""
        # check to see if it works when a block is tampered with
        block = Block([Transaction(self.user1, self.user2, 500)])
        self.bc.add_block(block)
        # tamper the first block by changing the amount to 1000
        self.bc._blockchain[0].transactions[0].amount = 1000
        # test to see that the returned tampered list contains the first block
        self.assertEqual(self.bc.validate_chain(), ['Block(transactions=[Transaction(from_user=ROOT, to_user=ROOT, amount=1000)], previous_hash=None)'])


unittest.main()