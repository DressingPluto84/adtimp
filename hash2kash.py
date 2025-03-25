class LinkedList:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value

class HashTableChaining:
    def __init__(self):
        self.table = [None] * 31

    def _hasher(self, obj):
        return obj % 31

    def HashInsert(self, obj):
        k = self._hasher(obj)
        jit = LinkedList(obj)
        if self.table[k] == None:
            self.table.insert(k, jit)
        else:
            jit.next = self.table[k]
            self.table[k].prev = jit
            self.table[k] = jit

    def HashSearch(self, obj):
        k = self._hasher(obj)
        if self.table[k] == None:
            return False
        curr = self.table[k]
        while curr != None:
            if curr.val == obj:
                return True
            curr = curr.next
        return False

    def HashDelete(self, obj):
        k = self._hasher(obj)
        curr = self.table[k]
        while curr != None:
            if curr.val == obj:
                if curr.prev == None:
                    self.table[k] = curr.next
                else:
                    curr.prev.next = curr.next
                    curr.prev = None
                    curr.next = None
            curr = curr.next

class HashTableOpenAddressing:
    def __init__(self):
        self.table = [None] * 31

    def _hasher1(self, obj):
        return obj % 31

    def _hasher2(self, obj):
        return obj % 8 + 9

    def HashInsert(self, obj):
        k = self._hasher1(obj)
        if self.table[k] != None:
            i = 1
            while self.table[k] != None and k < 30:
                k = (k + i * self._hasher2(obj)) % 31
                i += 1
            if k > 30:
                return False
            self.table[k] = obj

    def HashSearch(self, obj):
        k = self._hasher1(obj)
        if self.table[k] != obj:
            i = 1
            while self.table[k] != obj and k < 30:
                k = (k + i * self._hasher2(obj)) % 31
                i += 1
            if k > 30:
                return False
            return True

    def HashDelete(self, obj):
        k = self._hasher1(obj)
        if self.table[k] != obj:
            i = 1
            while self.table[k] != obj and k < 30:
                k = (k + i * self._hasher2(obj)) % 31
                i += 1
            if k > 30:
                return
            self.table[k] = None

hashir = HashTableChaining()
hashir.HashInsert(1)
hashir.HashInsert(19)
print(hashir.HashSearch(1))
print(hashir.HashSearch(19))
hashir.HashDelete(19)
print(hashir.HashSearch(19))

