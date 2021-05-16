#used for hashing 
import hashlib

class CrypticCashBlock:
    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

#transaction example 
transaction_1 = "Anna sends 2 SC to Mike"
transaction_2 = "Bob sends 4.1 SC to Mike"
transaction_3 = "Mike sends 3.2 SC to Bob"
transaction_4 = "Dan sends 0.3 SC to Anna"
transaction_5 = "Mike sends 1 SC to Ram"
transaction_6 = "Mike sends 5.4 SC to Dan"

initial_block = CrypticCashBlock("Initial String",[transaction_1,transaction_2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = CrypticCashBlock(initial_block.block_hash,[transaction_3,transaction_4])

print(second_block.block_data)
print(second_block.block_hash)