class PriorityQueue:
    
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def insert(self, data):
        self.data = data
        self.queue.append(self.data)

    def delete(self):
        max = 0

        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max]:
                max = i
            
        item = self.queue[max]
        del self.queue[max]
        return item    

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
            

priority_queue = PriorityQueue()

priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(12)
priority_queue.insert(5)
priority_queue.insert(15)

print(priority_queue)

while not priority_queue.is_empty():
    print(priority_queue.delete())