class Node:
    def __init__(self, key=-1):
        self.key = key
        self.next = None

# Class for circular linked list
class LinkedList:
    def __init__(self, key):
        self.head = Node()
        self.head.key = key
        self.head.next = self.head

    def insert_node(self, key):
        newNode = Node(key)
        p = self.head
        s = p.next
        while s.key <= key and s != self.head:
            p = p.next
            s = p.next
        p.next = newNode
        newNode.next = s

    def delete_node(self, key):
        p = self.head
        s = p.next
        # If we need to delete head
        if key == p.key:
            if s == self.head:
                return -1
            else:
                while True:
                    if s.next == self.head:
                        s.next = self.head.next
                        self.head = s.next
                        return key
                    else:
                        s = s.next
        # delete except head node
        while s.key != key and s != self.head:
            p = p.next
            s = p.next
        if s != self.head:
            p.next = s.next
            return key
        else:
            return -1

    # method for josephus problem
    def josephus(self, step):
        s = self.head
        while(True):
            print(s.key, "->", end=" ")
            self.delete_node(s.key)
            for i in range(step):
                s = s.next
            if s == self.head:
                print(s.key)
                break

    def print_node(self):
        p = self.head
        print("Start", p.key, "->", end=" ")
        p = p.next
        while p != self.head:
            print(p.key, "->", end=" ")
            p = p.next
        print("End")


#main() function
if __name__ == "__main__":
    totalcount = int(input("Input total node's count : "))
    step = int(input("Input step for josephus's problem : "))

    list = LinkedList('A')
    # Already insert 'A' for header. So we only need to insert_node (totalcount-1)
    for i in range(totalcount-1):
        list.insert_node(chr(ord('B')+i))
    list.josephus(step)
