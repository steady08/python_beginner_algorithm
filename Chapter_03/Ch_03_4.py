class Node:
    def __init__(self, key=-1):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.next = self.tail

    def ordered_insert(self, key):
        newNode = Node(key)
        p = self.head
        s = p.next
        while s.key <= key and s != self.tail:
            p = p.next
            s = p.next
        p.next = newNode
        newNode.next = s

    def delete_node(self, key):
        p = self.head
        s = p.next
        while s.key != key and s != self.tail:
            p = p.next
            s = p.next
        if s != self.tail:
            p.next = s.next
            return True
        else:
            return False

    def print_node(self):
        p = self.head
        p = p.next
        print("Start", end=" ")
        while p != self.tail:
            print(p.key, "->", end=" ")
            p = p.next
        print("End")


#main() function
if __name__ == "__main__":
    list = LinkedList()
    list.ordered_insert(7)
    list.ordered_insert(8)
    list.ordered_insert(1)
    list.ordered_insert(9)
    list.print_node()

    list.delete_node(7)
    list.print_node()
