class Queue:

    def __init__(self):
        self.queue = list()

    # Adding elements to queue
    def enqueue(self, data):
        # Checking to avoid duplicate entry
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    # Removing the last element from the queue
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return "Queue Empty!"

    # Getting the size of the queue
    def size(self):
        return len(self.queue)


def queue_to_stack(queue_1, queue_2):
    if not queue_1.size() == 0:
        while queue_1.size() > 0:
            queue_2.enqueue(queue_1.dequeue())
        stack = queue_2.dequeue()
        while queue_2.size() > 0:
            queue_1.enqueue(queue_2.dequeue())
        return stack


if __name__ == "main":
    queue_1 = Queue()
    queue_2 = Queue()
    queue_1.enqueue(1)
    queue_1.enqueue(2)
    queue_1.enqueue(3)
    queue_1.enqueue(5)
    queue_1.enqueue(6)
    queue_to_stack(queue_1, queue_2)
