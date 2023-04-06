import hashmap

class Transaction():
    """Class that contains the user, reciever, and amount of the transaction"""
    def __init__(self, from_user, to_user, amount):
        """Initializes the transaction class"""
        self.from_user = from_user
        self.to_user = to_user 
        self.amount = amount

    def __repr__(self):
        """__repr__ method used to allow for validation of transaction taking place"""
        return f"Transaction(from_user={self.from_user}, to_user={self.to_user}, amount={self.amount})"
    
class Block():
    """Class that contains the transactions and previous hash"""
    def __init__(self, transactions=None, previous_hash = None):
        """Initializes the block class"""
        # initiliazes empty list to transactions
        if transactions is None: 
            self.transactions = []
        else: 
            self.transactions = transactions
        # initializes previous hash to none if no hash is given as a parameter
        self.previous_hash = previous_hash
    
    def add_transaction(self, transaction):
        """appends to the transactions list with the specific transaction being used"""
        # appends a transaction to the list
        self.transactions.append(transaction)

    def __repr__(self):
        """__repr__ is used which allows for greater organization inside the block"""
        return f"Block(transactions={self.transactions}, previous_hash={self.previous_hash})"
        
        

class Ledger():
    """Class that initializes a hashmap and performs multiple operations that deal with the amount of huskycoins in a person's account"""
    def __init__(self):
        """Initializes the ledger class"""
        self._hashmap = hashmap.HashMapping()

    def has_funds(self, user, amount):
        """checks to see if the user has enough funds to continue with their transaction"""
        # returns False if user is not in the hashmap
        if user not in self._hashmap:
            return False
        balance = self._hashmap[user]
        # checks to see if the user has enough money to make the transaction
        if balance >= amount:
            return True
        else:
            return False
    
    def deposit(self, user, amount):
        """Deposits a certain amount into a users acount"""
        # checks to see if user is in hashmap - if not - then amount user has is updated 
        if user not in self._hashmap:
            self._hashmap[user] = amount
        else:
            self._hashmap[user] += amount

    def transfer(self, user, reciever, amount):
        """transfers a certain amount from the user to the reciever"""
        # checks to see if the user has enough funds to make the transaction
        if self.has_funds(user, amount):
            self._hashmap[user] -= amount
            self.deposit(reciever, amount)
            return True
        else:
            return False
    
    def __repr__(self):
        """Allows for easier testing"""
        return f"Ledger(_hashmap={self._hashmap})"
    
    def __hash__(self):
        """Allows for hashing with the self._hashmap"""
        return hash(self._hashmap)
 

class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to 
        provide initial balances to one or more users.'''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    # TODO - add the rest of the code for the class here
    def add_block(self, block):
        """Adds a block to the blockchain """
        # Get the hash of the last block in the chain
        previous_hash = hash(self._blockchain[-1]) if self._blockchain else None

        # Set the previous hash of the new block
        block.previous_hash = previous_hash

        # Add the new block to the chain
        self._blockchain.append(block)

        # Update the ledger with the transactions in the new block
        for transaction in block.transactions:
            self._bc_ledger.transfer(transaction.from_user, transaction.to_user, transaction.amount)

        return True


    def validate_chain(self):
        """compares hashes in order to see if there is any tampering with the blocks"""

        # creates an empty list
        tampered_blocks = []

        # checks to see if the length of the blockchain is zero - returns False as no alterations can be done
        if len(self._blockchain) == 0:
            return False
        
        # for loop created - iterates through the blockchain and compares the hash of the block with the hash stored in the next block
        for i in range(0, len(self._blockchain)):
            if hash(self._blockchain[i]) != self._blockchain[i-1].previous_hash:
                tampered_blocks.append(str(self._blockchain[i-1]))

        # returns list of tampered blocks
        return tampered_blocks

    def __hash__(self):
        """hashes the blockchain"""
        # allow for hashing of a block
        return hash(self._blockchain)
    
    def __repr__(self):
        """allows for easier testing by printing out the blockchain and ledger"""
        # provides an output for the blockchain
        return f"Blockchain(_blockchain={self._blockchain}, _bc_ledger={self._bc_ledger})"
