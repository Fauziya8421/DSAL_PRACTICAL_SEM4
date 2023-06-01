# Consider a telephone book database of N clients. Make use of a hash table implementation
# to quickly look up client‘s telephone number. Make use of two collision handling
# techniques and compare them using number of comparisons required to find aset of
# telephone numbers (Python)

class Client:
    def __init__(self, name, telephone):
        self.name = name
        self.telephone = telephone

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert_separate_chaining(self, client):
        hash_value = self.hash_function(client.name)
        bucket = self.table[hash_value]
        bucket.append(client)

    def insert_linear_probing(self, client):
        hash_value = self.hash_function(client.name)
        while self.table[hash_value]:
            hash_value = (hash_value + 1) % self.size
        self.table[hash_value] = client

    def find_separate_chaining(self, name):
        hash_value = self.hash_function(name)
        bucket = self.table[hash_value]
        for client in bucket:
            if client.name == name:
                return client.telephone
        return None

    def find_linear_probing(self, name):
        hash_value = self.hash_function(name)
        while self.table[hash_value]:
            if self.table[hash_value].name == name:
                return self.table[hash_value].telephone
            hash_value = (hash_value + 1) % self.size
        return None


# Create a sample set of clients
clients = [
    Client("John Doe", "1234567890"),
    Client("Jane Smith", "9876543210"),
    Client("Alice Johnson", "4567890123"),
    Client("Bob Williams", "7890123456"),
    Client("Eva Davis", "2345678901"),
]

# Initialize hash tables for separate chaining and linear probing
hash_table_separate_chaining = HashTable(10)
hash_table_linear_probing = HashTable(10)

# Insert clients into the hash tables
for client in clients:
    hash_table_separate_chaining.insert_separate_chaining(client)
    hash_table_linear_probing.insert_linear_probing(client)

# Find telephone numbers using separate chaining
separate_chaining_comparisons = 0
for client in clients:
    telephone = hash_table_separate_chaining.find_separate_chaining(client.name)
    separate_chaining_comparisons += 1

# Find telephone numbers using linear probing
linear_probing_comparisons = 0
for client in clients:
    telephone = hash_table_linear_probing.find_linear_probing(client.name)
    linear_probing_comparisons += 1

# Print the number of comparisons required for each technique
print("Separate Chaining Comparisons:", separate_chaining_comparisons)
print("Linear Probing Comparisons:", linear_probing_comparisons)
