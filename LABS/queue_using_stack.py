class CustomQueue:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, x):
        self.stack_enqueue.append(x)

    def dequeue(self):
        # if stack dequeue is empty , transfer elements from stack enqueue
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        # if stack is still empty ,queue is empty
        if not self.stack_dequeue:
            return "Queue is empty"

        # pop the front element from stack dequeue
        return self.stack_dequeue.pop()

    def print_front(self):
        # if stack dequeue is empty transfer from stack enqueue
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        # if stack dequeue is still empty
        if not self.stack_dequeue:
            return "Queue is empty"

        # return the front element from stack dequeue without removing it
        return self.stack_dequeue[-1]


queue = CustomQueue()
query = input()
query_arr = query.split(",")

for i in query_arr:
    if i[0] == "1":
        command, x = i.split()
        queue.enqueue(int(x))
    elif i[0] == "2":
        result = queue.dequeue()
        print(result)
    elif i[0] == "3":
        result = queue.print_front()
        print(result)
