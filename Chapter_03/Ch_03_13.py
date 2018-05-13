# Circular Queue using List
class QueueWithArray:
    def __init__(self):
        MAX_NUM_OF_LIST = 10
        self.front = 0
        self.rear = 0
        self.queue = []
        for i in range(MAX_NUM_OF_LIST):
            self.queue.append(0)
        self.max_num_of_list = MAX_NUM_OF_LIST

    def init_queue(self):
        self.front = self.rear = 0

    def clear_queue(self):
        self.front = self.rear

    def put(self, data):
        if (self.rear + 1) % self.max_num_of_list == self.front:
            print("Queue overflow")
            return False
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.max_num_of_list

        return data

    def get(self):
        if self.front == self.rear:
            print("Queue underflow")
            return False
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.max_num_of_list

        return data

    def print_queue(self):
        print("Queue contents : Front ----> Rear")
        i = self.front
        while i != self.rear:
            print(self.queue[i], end= " ")
            i = (i + 1) % self.max_num_of_list
        print()


# main() function
if __name__ == "__main__":
    queue = QueueWithArray()
    queue.init_queue()

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

    print("Now queue is full, put 3")
    queue.put(3)
    queue.print_queue()

    print("Initialize queue")
    queue.clear_queue()
    queue.print_queue()

    print("Now queue is empty, get")
    data = queue.get()
    queue.print_queue()
    print("Getting value is ", data)