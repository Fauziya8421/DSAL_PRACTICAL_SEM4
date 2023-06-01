# Implement all the functions of a dictionary (ADT) using hashing and handle collisions using
# chaining with /without replacement.
# Data: Set of (key, value) pairs, Keys are mapped to values, Keys
# must be comparable, Keys must be unique
# Standard Operations: Insert(key, value),
# Find(key), Delete(key) (python)

class Dictionary:
    def __init__(self):
        self.size = 10  # Choose an appropriate size for the hash table
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_value = self.hash_function(key)
        bucket = self.table[hash_value]
        for pair in bucket:
            if pair[0] == key:
                raise ValueError("Duplicate key: {}".format(key))
        bucket.append((key, value))

    def find(self, key):
        hash_value = self.hash_function(key)
        bucket = self.table[hash_value]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        hash_value = self.hash_function(key)
        bucket = self.table[hash_value]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return
        raise KeyError("Key not found: {}".format(key))

# Create a dictionary
dictionary = Dictionary()

# Insert key-value pairs
dictionary.insert("apple", "A fruit")
dictionary.insert("banana", "A fruit")
dictionary.insert("carrot", "A vegetable")

# Find values by key
print(dictionary.find("apple"))  # Output: A fruit
print(dictionary.find("banana"))  # Output: A fruit
print(dictionary.find("carrot"))  # Output: A vegetable
print(dictionary.find("mango"))  # Output: None

# Delete keys
dictionary.delete("apple")
print(dictionary.find("apple"))  # Output: None
