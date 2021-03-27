import hashlib


class Block:
    def __init__(self, previous, transaction):
        self.transactions = transaction
        self.previous = previous
        string_to_hash = transaction + previous
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()
