class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] =data

        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = self.data #replace

            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] !=None and self.slots[nextslot] != key:
                   nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data #replace

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        found = False
        position = startslot
        stop = False
        data = None

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def rehash(self, oldkey, size):
        return ((oldkey+1)%size)

    def hashfunction(self, key, size):
        return key%size


H = HashTable()
H[26] = "dog"
H[32] = "cat"
H[23] = "Dog"
print(H.slots)
print(H[33])
