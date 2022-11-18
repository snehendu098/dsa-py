# 98, 85, 89, 10, 15, 45, 89
#  0   1   2   3   4   5   6
#      R  F
# (self.rear + 1) % self.size = self.front
# This checks if the queue is full

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is full")
            return
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):
            print("Queue is empty")
            return
        elif(self.front == self.rear):
            popVal = self.queue[self.rear]
            self.front = -1
            self.rear = -1
            return popVal
        else:
            popVal = self.queue(self.front)
            self.front = (self.front + 1) % self.size
            return popVal
