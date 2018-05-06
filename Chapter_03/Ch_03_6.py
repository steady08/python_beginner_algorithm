class Node:
    def __init__(self, key=-1):
        self.key = key
        self.prev = None
        self.next = None

# Class for doubly linked list
class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.head.prev = self.head
        self.tail.next = self.tail
        self.tail.prev = self.head

    # Insert new node ahead of tNode
    def insert_dnode_ptr(self, key, tNode):
        if tNode == self.head:
            return None
        iNode = Node(key)
        tNode.prev.next = iNode
        iNode.prev = tNode.prev
        tNode.prev = iNode
        iNode.next = tNode

        return iNode

    def delete_dnode_ptr(self, tNode):
        # Can't remove head and tail
        if tNode == self.head or tNode == self.tail:
            return 0
        tNode.prev.next = tNode.next
        tNode.next.prev = tNode.prev

        return tNode

    def find_node(self, key):
        s = self.head.next
        while s.key != key and s != self.tail:
            s = s.next
        if s == self.tail:
            return False
        else:
            return s

    def delete_dnode(self, key):
        s = self.find_node(key)
        if s != self.tail:
            s.prev.next = s.next
            s.next.prev = s.prev
            return True
        return False

    def insert_dnode(self, key, tNode):
        s = self.find_node(tNode)
        if s != self.tail:
            i = Node(key)
            s.prev.next = i
            i.prev = s.prev
            s.prev = i
            i.next = s
            return i
        return Null

    def ordered_insert(self, key):
        s = self.head.next
        while s.key <= key and s != self.tail:
            s = s.next
        i = Node(key)
        s.prev.next = i
        i.prev = s.prev
        s.prev = i
        i.next = s

        return i

    def delete_all(self):
        self.tail = self.head.next
        self.head = self.tail.prev

    def print_all(self):
        p = self.head
        print("Start", end=" ")
        p = p.next
        while p != self.tail:
            print(p.key, "->", end=" ")
            p = p.next
        print("End")


#main() function
if __name__ == "__main__":
    list = LinkedList()
    list.ordered_insert(10)
    list.ordered_insert(5)
    list.ordered_insert(8)
    list.ordered_insert(3)
    list.ordered_insert(1)
    list.ordered_insert(7)
    list.ordered_insert(8)

    print("Initial linked list is")
    list.print_all()

    print()
    findNumber = 4
    if list.find_node(findNumber) != False:
        print("Finding %d is successful" % findNumber)
    else:
        print("Finding %d is unsuccessful" % findNumber)

    print()
    findNumber = 5
    t = list.find_node(findNumber)
    if t != False:
        print("Finding %d is successful" % findNumber)
    else:
        print("Finding %d is unsuccessful" % findNumber)

    print()
    print("Inserting 7 before 5")
    list.insert_dnode_ptr(7, t)
    list.print_all()

    print()
    findNumber = 3
    t = list.find_node(findNumber)
    if t != False:
        print("Finding %d is successful and Deleting" % findNumber)
        list.delete_dnode_ptr(t)
    else:
        print("Finding %d is unsuccessful" % findNumber)
    list.print_all()

    print()
    findNumber = 10
    t = list.find_node(findNumber)
    if t != False:
        print("Finding %d is successful" % findNumber)
        print("Inserting 2 before %d" % findNumber)
        list.insert_dnode_ptr(2, t)
    else:
        print("Finding %d is unsuccessful" % findNumber)
    list.print_all()

    print()
    findNumber = 2
    t = list.find_node(findNumber)
    if t != False:
        print("Finding %d is successful and Deleting" % findNumber)
        list.delete_dnode_ptr(t)
    else:
        print("Finding %d is unsuccessful" % findNumber)
    list.print_all()

    print()
    findNumber = 1
    t = list.find_node(findNumber)
    if t != False:
        print("Finding %d is successful and Deleting" % findNumber)
        list.delete_dnode_ptr(t)
    else:
        print("Finding %d is unsuccessful" % findNumber)
    list.print_all()

    print()
    print("Inserting 15 at last")
    list.insert_dnode_ptr(15, list.head.next)
    list.print_all()

    print()
    print("Delete all node")
    list.delete_all()
    list.print_all()
