# Queue using Double linked list
class Node:
    def __init__(self, key=-1):
        self.key = key
        self.prev = None
        self.next = None


class QueueWithDoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.prev = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = self.tail

    def put(self, data):
        new_node = Node()
        new_node.key = data
        # Insert new_node in front of tail
        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        self.tail.prev = new_node
        new_node.next = self.tail

        return data

    def get(self):
        t = self.head.next
        if t == self.tail:
            print("Queue underflow")
            return False
        data_temp = t.key
        # Remove node
        self.head.next = t.next
        t.next.prev = self.head

        return data_temp

    def clear_queue(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def print_queue(self):
        t = self.head.next
        print("Queue contents : Front ----> Rear")
        while t != self.tail:
            print(t.key, end=" ")
            t = t.next
        print()


# main() function
if __name__ == "__main__":
    queue = QueueWithDoubleLinkedList()

    print("Put 5, 4, 7, 8, 2, 1")
    queue.put(5)
    queue.put(4)
    queue.put(7)
    queue.put(8)
    queue.put(2)
    queue.put(1)
    queue.print_queue()

    print("Get")
    data = queue.get()
    queue.print_queue()
    print("Getting value is ", data)

    print("Put 3, 2, 5, 7")
    queue.put(3)
    queue.put(2)
    queue.put(5)
    queue.put(7)
    queue.print_queue()

    print("Initialize queue")
    queue.clear_queue()
    queue.print_queue()

    print("Now queue is empty, get")
    data = queue.get()
    queue.print_queue()
    print("Getting value is ", data)