class Queue:
    def __init__(self):
        self.values = []
    
    def enqueue(self, x):
        self.values.append(x)  # Add element to the back of the queue
    
    def dequeue(self):
        if not self.is_empty():
            front = self.values.pop(0)  # Remove and return the front element
            return front
        else:
            return "Queue is empty"
    
    def is_empty(self):
        return len(self.values) == 0  # Check if the queue is empty
    
    def peek(self):
        if not self.is_empty():
            return self.values[0]  # Return the front element without removing
        else:
            return "Queue is empty"

# Test the Queue class
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Queue values:", q.values)  # Output: [10, 20, 30, 40]
print("Front element:", q.peek())  # Output: 10
print("Dequeue:", q.dequeue())     # Output: 10 (removes 10 from the queue)
print("Queue after dequeue:", q.values)  # Output: [20, 30, 40]
