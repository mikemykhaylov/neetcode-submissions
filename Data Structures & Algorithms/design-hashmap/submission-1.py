class Node:
    def __init__(self):
        self.key = -1
        self.value = -1
        self.next = None

def hash(value: int) -> int:
        return value % 1000

class MyHashMap:
    def __init__(self):
        self.arr = [Node() for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        hashkey = hash(key)
        node = self.arr[hashkey]
        while node.next != None:
            if node.key == -1:
                node.key = key
            if node.key == key:
                node.value = value
                return
            node = node.next
        node.key = key
        node.value = value
        node.next = Node()
        

    def get(self, key: int) -> int:
        hashkey = hash(key)
        node = self.arr[hashkey]
        while node.next != None:
            if node.key == key:
                return node.value
            node = node.next

        return node.value

    def remove(self, key: int) -> None:
        hashkey = hash(key)
        node = self.arr[hashkey]
        while node.next != None:
            if node.key == key:
                node.key = -1
                node.value = -1
                break
            node = node.next    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)