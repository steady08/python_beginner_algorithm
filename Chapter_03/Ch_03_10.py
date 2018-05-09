# Stack with linked list
class Node:
    def __init__(self, key=-1):
        self.key = key
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.next = self.tail

    def push(self, i):
        new_node = Node(i)
        new_node.key = i
        # Input to head side
        new_node.next = self.head.next
        self.head.next = new_node

        return i

    def pop(self):
        # Output to head side
        t = self.head.next
        # Stack empty case
        if t == self.tail:
            return -1

        output = t.key
        self.head.next = t.next

        return output

    def clear_stack(self):
        # Python manage memory automatically
        self.head.next = self.tail

    def print_stack(self):
        p = self.head.next
        print("Stack contents : Top : ", end=" ")
        while p != self.tail:
            print(p.key, "->", end=" ")
            p = p.next
        print(" : Bottom")


#main() function
if __name__ == "__main__":
    stack = Stack()

    print("Push 5, 4, 7, 8, 2, 1")
    stack.push(5)
    stack.push(4)
    stack.push(7)
    stack.push(8)
    stack.push(2)
    stack.push(1)
    stack.print_stack()

    print("Pop")
    i = stack.pop()
    stack.print_stack()
    print("Poped value is : ", i)

    # Don't test for memory full case

    print("Initialize stack")
    stack.clear_stack()
    stack.print_stack()

    print("Now stack is empty, pop")
    i = stack.pop()
    stack.print_stack()
    print("Poped value is : ", i)


