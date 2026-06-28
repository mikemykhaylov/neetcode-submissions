from typing import TypedDict

class Node:
    val: int
    children: list[Node]
    final: bool
    def __init__(self, val):
        self.val = val
        self.children = [None] * 10
        self.final = False


class MyHashSet:
    root: Node
    def __init__(self):
        self.root = Node(0)

    def add(self, key: int) -> None:
        node = self.root
        while key >= 0:
            remainder = key % 10
            intdiv = key // 10
            if node.children[remainder] == None:
                node.children[remainder] = Node(remainder)
            node = node.children[remainder]
            if intdiv == 0:
                break
            key = intdiv          
        node.final = True


    def remove(self, key: int) -> None:
        prev = None
        node = self.root
        remainder = intdiv = 0
        while key >= 0:
            remainder = key % 10
            intdiv = key // 10
            if node.children[remainder] == None:
                return
            prev = node
            node = node.children[remainder]
            if intdiv == 0:
                break
            key = intdiv
        for child in node.children:
            if child != None:
                node.final = False
                return
        prev.children[remainder] = None

    def contains(self, key: int) -> bool:
        node = self.root
        remainder = intdiv = 0
        while key >= 0:
            remainder = key % 10
            intdiv = key // 10
            if node.children[remainder] == None:
                return False
            node = node.children[remainder]
            if intdiv == 0:
                break
            key = intdiv
        return node.final

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)