class Queue:
  
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size

    def enqueue(self, val):
        if self.rear == self.size:
            print("Queue is Full")
        else:
            self.queue[self.rear] = val
            self.rear = self.rear + 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is Empty")
        else:
            print("Dequeued element  = ",self.queue[self.front])
            self.front = self.front + 1

if __name__=='__main__':

    q = Queue(3)

    q.dequeue()

    print("Enqueuing element: ",10)
    q.enqueue(10)
    print("Enqueuing element: ",20)
    q.enqueue(20)
    print("Enqueuing element: ",30)
    q.enqueue(30)
    print("Enqueuing element: ",40)
    q.enqueue(40)

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
