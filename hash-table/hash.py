class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self,string):
        return sum(ord(c) for c in string)  
     

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        self.collection[hash_value][key] = value

    def remove(self,key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]
                
                if not self.collection[hash_value]:
                    del self.collection[hash_value]
            

    def lookup(self,key):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            return None
        return self.collection[hash_value].get(key)

if __name__=="__main__":
    ht = HashTable()
    print(ht.hash('golf'))  

    ht.add('golf', 'sport')
    print(ht.collection)

    ht.add('dear', 'friend')
    ht.add('read', 'book')
    print(ht.collection)

    print(ht.lookup('golf'))

    print(ht.lookup('hello'))

    ht.remove('golf')
    print(ht.lookup('golf'))

    ht.add('fcc', 'coding')
    ht.add('cfc', 'chemical')
    print(ht.collection)
