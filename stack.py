class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1
        
    def push(self, key):
        if(self.top == self.size -1):
            print("Stack is full")
        else:
            self.top = self.top+1
            self.stack[self.top] = key
            
    def pop(self):
        if(self.top == -1):
            print("stack is empty")
        else:
            self.top = self.top - 1
            
s = Stack(3)

s.pop()

print("Pushing element: ",10)
s.push(10)
print("Pushing element: ",20)
s.push(20)
print("Pushing element: ",30)
s.push(30)
print("Pushing element: ",40)
s.push(40)

s.pop()
s.pop()
s.pop()
s.pop()
        
