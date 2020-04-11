# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hashvalue = 5381
        for c in key:
            hashvalue = (hashvalue * 33) + ord(c)
        return hashvalue

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        '''
        index = self._hash_mod(key)
        first_linked_pair = LinkedPair(key, value)
        if self.storage[index]:
            first_linked_pair.next = self.storage[index]
        self.storage[index] = first_linked_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        '''
        index = self._hash_mod(key)
        found = False

        if self.storage[index]:
            pair = self.storage[index]

            if pair.key == key:
                self.storage[index] = pair.next
            else:
                while pair.next and not found:
                    if pair.next.key == key:
                        pair.next = pair.next.next
                        found = True
                    pair = pair.next
        if not found:
            print(f'Key: {key} wasn\'t found')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        '''
        index = self._hash_mod(key)
        value = None
        if self.storage[index]:
            pair = self.storage[index]

            while not value:
                if pair.key == key:
                    value = pair.value
                else:
                    pair = pair.next
        return value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        self.capacity *= 2
        old_storage = self.storage
        self.storage = [None] * self.capacity

        for pair in old_storage:
            while pair:
                self.insert(pair.key, pair.value)
                pair = pair.next
        
if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
